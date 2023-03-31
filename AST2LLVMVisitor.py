from AST import *
import graphviz
from SymbolTable import *
import struct

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class AST2LLVMVisitor(Visitor):

    llvm = ""
    symbolTable = 0
    instr = 1
    intprinting = False
    floatprinting = False
    charprinting = False
    printing = False

    def __init__(self, llvm="", symbolTable=SymbolTable()):
        #print("----------------Converting AST 2 LLVM IR----------------")
        self.llvm = llvm
        self.symbolTable = symbolTable

    def VisitASTNode(self, currentNode):
        #print("Node")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitBinaryOperation(self, currentNode):
        #print("Binary")
        for child in currentNode.children:
            node = child.accept(self)
        return "binary"

    def VisitUnaryOperation(self, currentNode):
        #print("Unary")
        match currentNode.value:
            case "&":
                node = currentNode.children[0].accept(self)
                return "%"+self.symbolTable.lookup(node.value).register
            case "*":
                node = currentNode.children[0].accept(self)
                for child in currentNode.children:
                    node = child.accept(self)

                    if isinstance(node, ASTNode):
                        match self.symbolTable.lookup(node.value).type:
                            case "int*":
                                self.llvm += "%" + str(self.instr) + " = load i32*, i32** %" + str(self.symbolTable.lookup(node.value).register) + ", align 8\n"
                                self.instr += 1
                                return "%"+self.symbolTable.lookup(node.value).register
                            case "float*":
                                self.llvm += "%" + str(self.instr) + " = load float*, float** %" + str(
                                    self.symbolTable.lookup(node.value).register) + ", align 8\n"
                                self.instr += 1
                                return "%" + self.symbolTable.lookup(node.value).register
                            case "char*":
                                self.llvm += "%" + str(self.instr) + " = load i8*, i8** %" + str(
                                    self.symbolTable.lookup(node.value).register) + ", align 8\n"
                                self.instr += 1
                                return "%" + self.symbolTable.lookup(node.value).register
                    else:
                        self.llvm += "%" + str(self.instr) + " = load i32*, i32** %" + str(self.instr-1) + ", align 8\n"
                        self.instr += 1;
                        return node
            case other:
                print("not implemented yet")
        return currentNode

    def VisitRelationOperation(self, currentNode):
        #print("Relation")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitLogicalOperation(self, currentNode):
        #print("Logical")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitConstant(self, currentNode):
        #print("Constant")
        #self.llvm+= " "+currentNode.value
        return currentNode.value

    def VisitDeclaration(self, currentNode):
        #print("Declaration2LLVM")
        var = currentNode.var
        type = currentNode.type
        attr = currentNode.attr
        match type:
            case "int":
                self.llvm += "%" + str(self.instr) + " = alloca i32, align 4\n"
                self.symbolTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case "float":
                self.llvm += "%" + str(self.instr) + " = alloca float, align 4\n"
                self.symbolTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case "char":
                self.llvm += "%" + str(self.instr) + " = alloca i8, align 1\n"
                self.symbolTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case "int*":
                self.llvm += "%" + str(self.instr) + " = alloca i32*, align 8\n"
                self.symbolTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case "float*":
                self.llvm += "%" + str(self.instr) + " = alloca float*, align 8\n"
                self.symbolTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case "char*":
                self.llvm += "%" + str(self.instr) + " = alloca i8*, align 8\n"
                self.symbolTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case other:
                x = "test"
                #print("Type not implemented or literal")

        return currentNode

    def VisitAssignment(self, currentNode):
        #print("Assignment2LLVM")


        if isinstance(currentNode.lvalue, Declaration):
            currentNode.lvalue.accept(self)
            value = currentNode.rvalue.accept(self)
            ltype = self.symbolTable.lookup(currentNode.lvalue.var).type
            if "%" not in value:
                if ltype == "int":
                    try:
                        value = int(value)
                    except ValueError:
                        value = float(value)
                    if isinstance(value, float) or isinstance(value, int):
                        self.llvm += "store i32 " + str(value) + ", i32* %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "float":
                    try:
                        value = float(value)
                    except ValueError:
                        print("failiure")
                    self.llvm += "store float " + str(value) + ", float* %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "char":
                    value = value.replace("'","")
                    #char = list(value)
                    #print(ord(char[0]))
                    self.llvm += "store i8 " + str(ord(value)) + ", i8* %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 1\n"
            else:
                if ltype == "int*":
                    self.llvm += "store i32* " + str(value) + ", i32** %" + self.symbolTable.lookup(
                        currentNode.lvalue.var).register + ", align 8\n"
                elif ltype == "float*":
                    self.llvm += "store float* " + str(value) + ", float** %" + self.symbolTable.lookup(
                        currentNode.lvalue.var).register + ", align 8\n"
                elif ltype == "char*":
                    self.llvm += "store i8* " + str(value) + ", i8** %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 8\n"
                elif ltype == "int":
                    self.llvm += "%" + str(self.instr) + " = load i32, i32 %" + str(self.instr - 1) + ", align 8\n"
                    self.instr +=1
                    self.llvm += "store i32 %" + str(self.instr - 1) + ", i32* %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "float":
                    self.llvm += "%" + str(self.instr) + " = load float, float %" + str(self.instr - 1) + ", align 8\n"
                    self.instr +=1
                    self.llvm += "store float %" + str(self.instr - 1) + ", float* %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "char":
                    value = value.replace("'","")
                    self.llvm += "%" + str(self.instr) + " = load i8, ptr %" + str(self.instr - 1) + ", align 8\n"
                    self.instr +=1
                    self.llvm += "store i8 %" + str(self.instr - 1) + ", i8* %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 1\n"
                else:
                    print("test")
        else:
            value = currentNode.rvalue.accept(self)
            reg = currentNode.lvalue.accept(self)
            ltype = self.symbolTable.lookup(currentNode.lvalue.children[0].value).type
            #self.instr += 1
            if ltype == "int*":
                #self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(reg) + ", align 8\n"
                try:
                    value = int(value)
                except ValueError:
                    value = float(value)
                if isinstance(value, float) or isinstance(value, int):
                    self.llvm += "store i32 " + str(value) + ", i32* %" + str(self.instr-1) + ", align 4\n"
            if ltype == "float*":
                #self.llvm += "%" + str(self.instr) + " = load float, float* " + str(reg) + ", align 8\n"
                try:
                    value = int(value)
                except ValueError:
                    value = float(value)
                if isinstance(value, float) or isinstance(value, int):
                    #print(self.instr - 1)
                    self.llvm += "store float " + str(value) + ", float* %" + str(self.instr-1) + ", align 4\n"
            if ltype == "char*":
                value = value.replace("'", "")
                self.llvm += "%" + str(self.instr) + " = load i8*, i8** " + str(reg) + ", align 8\n"
                self.llvm += "store i8 " + str(ord(value)) + ", i8* %" + str(self.instr-1) + ", align 1\n"
                self.instr += 1

        return currentNode

    def VisitMLComment(self, currentNode):
        #print("MLComment")
        comment = currentNode.value
        comment = comment.replace("/*",";")
        comment = comment.replace("*/", ";")
        comment = comment.replace("* ", "; ")
        self.llvm += comment + "\n"
        return currentNode

    def VisitSLComment(self, currentNode):
        #print("SLComment")
        comment = currentNode.value
        comment = comment.replace("//", ";")
        self.llvm += comment + "\n"
        return currentNode

    def VisitPrintf(self, currentNode):
        #print("Printf")
        node = currentNode.children[0].accept(self)
        symbol = self.symbolTable.lookup(node.value)
        if symbol:
            if not self.printing:
                self.llvm = "declare i32 @printf(i8* noundef, ...)\n" + self.llvm
            match symbol.type:
                case "int":
                    if not self.intprinting:
                        self.llvm = "@.int = private unnamed_addr constant [3 x i8] c" + "\"" + "%d" + "\\00" + "\", align 1\n"\
                                 + self.llvm
                        self.intprinting = True
                        self.printing = True

                    self.llvm += "%"+ str(self.instr) + " = load i32, i32* %" + str(symbol.register) + ", align 4\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                 "@.int, i64 0, i64 0), i32 noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
                case "float":
                    if not self.floatprinting:
                        self.llvm = "@.float = private unnamed_addr constant [3 x i8] c" + "\"" + "%f" + "\\00" + "\", align 1\n"\
                                     + self.llvm
                        self.floatprinting = True
                        self.printing = True

                    self.llvm += "%" + str(self.instr) + " = load float, float* %" + str(symbol.register) + ", align 4\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = fpext float %" + str(int(self.instr) - 1) + " to double\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                 "@.float, i64 0, i64 0), double noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
                case "char":
                    if not self.charprinting:
                        self.llvm = "@.char = private unnamed_addr constant [3 x i8] c" + "\"" + "%c" + "\\00" + "\", align 1\n"\
                                     + self.llvm
                        self.charprinting = True
                        self.printing = True

                    self.llvm += "%" + str(self.instr) + " = load i8, i8* %" + str(symbol.register) + ", align 4\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = sext i8 %" + str(int(self.instr) - 1) + " to i32\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                 "@.char, i64 0, i64 0), i32 noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
        else:
            if '\'' not in node.value:
                try:
                    value = int(node.value)
                except ValueError:
                    value = float(node.value)
                if isinstance(value, int):
                    if not self.printing:
                        self.llvm = "declare i32 @printf(i8* noundef, ...)\n" + self.llvm
                    if not self.intprinting:
                        self.llvm = "@.int = private unnamed_addr constant [3 x i8] c" + "\"" + "%d" + "\\00" + "\", align 1\n" \
                                    + self.llvm
                        self.intprinting = True
                        self.printing = True


                    self.llvm += "%" + str(self.instr) + " = alloca i32, align 4\n"
                    self.instr += 1
                    self.llvm += "store i32 " + str(node.value) + ", i32* %" + str(self.instr - 1) + ", align 4\n"
                    self.llvm += "%" + str(self.instr) + " = load i32, i32* %" + str(self.instr - 1) + ", align 4\n"
                    self.instr += 1
                    self.llvm += "%" + str(
                        self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                      "@.int, i64 0, i64 0), i32 noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
                elif isinstance(value, float):
                    if not self.printing:
                        self.llvm = "declare i32 @printf(i8* noundef, ...)\n" + self.llvm
                    if not self.floatprinting:
                        self.llvm = "@.float = private unnamed_addr constant [3 x i8] c" + "\"" + "%f" + "\\00" + "\", align 1\n" \
                                    + self.llvm
                        self.charprinting = True
                        self.printing = True

                    self.llvm += "%" + str(self.instr) + " = alloca float, align 4\n"
                    self.instr += 1
                    self.llvm += "store float " + str(node.value) + ", float* %" + str(self.instr - 1) + ", align 4\n"
                    self.llvm += "%" + str(self.instr) + " = load float, float* %" + str(self.instr - 1) + ", align 4\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = fpext float %" + str(int(self.instr) - 1) + " to double\n"
                    self.instr += 1
                    self.llvm += "%" + str(
                        self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                      "@.float, i64 0, i64 0), double noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
            else:
                value = node.value.replace("'", "")
                if not self.printing:
                    self.llvm = "declare i32 @printf(i8* noundef, ...)\n" + self.llvm
                if not self.charprinting:
                    self.llvm = "@.char = private unnamed_addr constant [3 x i8] c" + "\"" + "%c" + "\\00" + "\", align 1\n" \
                                + self.llvm
                    self.charprinting = True
                    self.printing = True

                self.llvm += "%" + str(self.instr) + " = alloca i8, align 4\n"
                self.instr += 1
                self.llvm += "store i8 " + str(ord(value)) + ", i8* %" + str(self.instr - 1) + ", align 4\n"
                self.llvm += "%" + str(self.instr) + " = load i8, i8* %" + str(self.instr - 1) + ", align 4\n"
                self.instr += 1
                self.llvm += "%" + str(self.instr) + " = sext i8 %" + str(int(self.instr) - 1) + " to i32\n"
                self.instr += 1
                self.llvm += "%" + str(
                    self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                  "@.char, i64 0, i64 0), i32 noundef %" + str(int(self.instr) - 1) + ")\n"
                self.instr += 1
        return currentNode


