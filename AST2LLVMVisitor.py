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

    def __init__(self, llvm="", symbolTable=SymbolTable()):
        print("----------------Converting AST 2 LLVM IR----------------")
        self.llvm = llvm
        self.symbolTable = symbolTable

    def VisitASTNode(self, currentNode):
        print("Node")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitBinaryOperation(self, currentNode):
        print("Binary")
        for child in currentNode.children:
            node = child.accept(self)
        return "binary"

    def VisitUnaryOperation(self, currentNode):
        print("Unary")
        match currentNode.value:
            case "&":
                node = currentNode.children[0].accept(self)
                return "%"+self.symbolTable.lookup(node.value).register
            case "*":
                node = currentNode.children[0].accept(self)
                if isinstance(node, ASTNode):
                    self.llvm += "%" + str(self.instr) + " = load ptr, ptr %" + str(self.symbolTable.lookup(node.value).register) + ", align 8\n"
                    self.instr += 1
                    return "%"+self.symbolTable.lookup(node.value).register
                else:
                    self.llvm += "%" + str(self.instr) + " = load ptr, ptr %" + str(self.instr-1) + ", align 8\n"
                    self.instr += 1;
                    return node
            case other:
                print("not implemented yet")
        return currentNode

    def VisitRelationOperation(self, currentNode):
        print("Relation")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitLogicalOperation(self, currentNode):
        print("Logical")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitConstant(self, currentNode):
        print("Constant")
        #self.llvm+= " "+currentNode.value
        return currentNode.value

    def VisitDeclaration(self, currentNode):
        print("Declaration2LLVM")
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
            case "int*" | "float*" | "char*":
                self.llvm += "%" + str(self.instr) + " = alloca ptr, align 8\n"
                self.symbolTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case other:
                print("Type not implemented or literal")

        return currentNode

    def VisitAssignment(self, currentNode):
        print("Assignment2LLVM")


        if isinstance(currentNode.lvalue, Declaration):
            currentNode.lvalue.accept(self)
            value = currentNode.rvalue.accept(self)
            print(value)
            ltype = self.symbolTable.lookup(currentNode.lvalue.var).type
            print("type=" + ltype)
            if "%" not in value:
                if ltype == "int":
                    try:
                        value = int(value)
                    except ValueError:
                        value = float(value)
                    if isinstance(value, float) or isinstance(value, int):
                        self.llvm += "store i32 " + str(value) + ", ptr %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "float":
                    try:
                        value = float(value)
                    except ValueError:
                        print("failiure")
                    self.llvm += "store float " + str(value) + " ptr %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "char":
                    value = value.replace("'","")
                    #char = list(value)
                    #print(ord(char[0]))
                    self.llvm += "store i8 " + str(ord(value)) + ", i8* %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 1\n"
            else:
                if ltype == "int*" or ltype == "float*" or ltype == "char*":
                    self.llvm += "store ptr " + str(value) + ", ptr %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 8\n"
                elif ltype == "int":
                    self.llvm += "%" + str(self.instr) + " = load i32, ptr %" + str(self.instr - 1) + ", align 8\n"
                    self.instr +=1
                    self.llvm += "store i32 %" + str(self.instr - 1)  + ", ptr %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "float":
                    self.llvm += "%" + str(self.instr) + " = load float, ptr %" + str(self.instr - 1) + ", align 8\n"
                    self.instr +=1
                    self.llvm += "store float %" + str(self.instr - 1) + ", ptr %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "char":
                    value = value.replace("'","")
                    self.llvm += "%" + str(self.instr) + " = load i8, ptr %" + str(self.instr - 1) + ", align 8\n"
                    self.instr +=1
                    self.llvm += "store i8 %" + str(self.instr - 1)  + ", i8* %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 1\n"
                else:
                    print("test")
        else:
            value = currentNode.rvalue.accept(self)
            print(value)
            reg = currentNode.lvalue.accept(self)
            ltype = self.symbolTable.lookup(currentNode.lvalue.children[0].value).type
            self.llvm += "%" + str(self.instr) + " = load ptr, ptr " + str(reg) + ", align 8\n"
            self.instr += 1
            if ltype == "int*":
                try:
                    value = int(value)
                except ValueError:
                    value = float(value)
                if isinstance(value, float) or isinstance(value, int):
                    print(self.instr - 1)
                    self.llvm += "store i32 " + str(value) + ", ptr %" + str(self.instr-1) + ", align 4\n"
            if ltype == "float*":
                try:
                    value = int(value)
                except ValueError:
                    value = float(value)
                if isinstance(value, float) or isinstance(value, int):
                    print(self.instr - 1)
                    self.llvm += "store float " + str(value) + ", ptr %" + str(self.instr-1) + ", align 4\n"
            if ltype == "char*":
                try:
                    value = int(value)
                except ValueError:
                    value = float(value)
                if isinstance(value, float) or isinstance(value, int):
                    print(self.instr - 1)
                    self.llvm += "store i8 " + str(value) + ", ptr %" + str(self.instr-1) + ", align 1\n"

        return currentNode

    def VisitMLComment(self, currentNode):
        print("MLComment")
        comment = currentNode.value
        comment = comment.replace("/*",";")
        comment = comment.replace("*/", ";")
        comment = comment.replace("* ", "; ")
        self.llvm += comment + "\n"
        return currentNode

    def VisitSLComment(self, currentNode):
        print("SLComment")
        comment = currentNode.value
        comment = comment.replace("//", ";")
        self.llvm += comment + "\n"
        return currentNode

    def VisitPrintf(self, currentNode):
        print("Printf")
        return currentNode


