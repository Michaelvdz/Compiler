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
        print(self.symbolTable)
        for key, value in self.symbolTable.vars.items():
            print(value.type)
            match value.type:
                case "int":
                    self.llvm += "%"+ str(self.instr) + " alloca i32, align 4 \n"
                    self.symbolTable.insertRegister(key, str(self.instr))
                case "float":
                    self.llvm += "%"+ str(self.instr) + " alloca float, align 4 \n"
                    self.symbolTable.insertRegister(key, str(self.instr))
                case "char":
                    self.llvm += "%"+ str(self.instr) + " alloca i8, align 1 \n"
                    self.symbolTable.insertRegister(key, str(self.instr))
                case other:
                    print("Type not implemented")
            self.instr +=1

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
        for child in currentNode.children:
            node = child.accept(self)
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
        print(var)
        type = currentNode.type
        print(type)
        attr = currentNode.attr
        print(attr)
        """
        self.llvm += "\n"
        self.llvm += "%" + var + " = "
        '''if attr == "const":
            self.llvm += " " + "contant"
        '''
        if type == "int":
            self.llvm += "alloca i32, align 4"
        elif type == "float":
            self.llvm += "alloca float, align 4"
        """
        return currentNode

    def VisitAssignment(self, currentNode):
        print("Assignment2LLVM")
        value = currentNode.rvalue.accept(self)
        currentNode.lvalue.accept(self)
        print(value)
        ltype = self.symbolTable.lookup(currentNode.lvalue.var).type
        print("type=" + ltype)
        if ltype == "int":
            print("yeeeeeeeeeeee")
            try:
                value = int(value)
            except ValueError:
                value = float(value)
            print(value)
            if isinstance(value, float) or isinstance(value, int):
                self.llvm += "store i32 " + str(value) + ", ptr %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 4"
        elif ltype == "float":
            try:
                value = float(value)
            except ValueError:
                print("failiure")
            self.llvm += "\nstore float " + str(value) + " ptr %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 4"
        elif ltype == "char":
            value = value.replace("'","")
            #char = list(value)
            #print(ord(char[0]))
            self.llvm += "\nstore i8 " + str(ord(value)) + ", i8* %" + self.symbolTable.lookup(currentNode.lvalue.var).register + ", align 1"
        else:
            print("test")
        return currentNode

    def VisitMLComment(self, currentNode):
        print("MLComment")
        comment = currentNode.value
        comment = comment.replace("/*",";")
        comment = comment.replace("*/", ";")
        comment = comment.replace("* ", "; ")
        self.llvm += comment
        return currentNode

    def VisitSLComment(self, currentNode):
        print("SLComment")
        comment = currentNode.value
        comment = comment.replace("//", " ;")
        self.llvm += comment
        return currentNode

    def VisitPrintf(self, currentNode):
        print("Printf")
        return currentNode


