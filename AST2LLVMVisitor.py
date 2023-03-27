from AST import *
import graphviz

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class AST2LLVMVisitor(Visitor):

    llvm = ""

    def __init__(self, llvm=""):
        print("----------------Converting AST 2 LLVM IR----------------")
        self.llvm = llvm

    def VisitASTNode(self, currentNode):
        print("Node")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitBinaryOperation(self, currentNode):
        print("Binary")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

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

    def VisitDeclaration(self, currentNode, value):
        print("Declaration2LLVM")
        var = currentNode.var
        print(var)
        type = currentNode.type
        print(type)
        attr = currentNode.attr
        print(attr)
        print(value)

        self.llvm += "%" + var + " dso_local"
        if attr == "const":
            self.llvm += " " + "contant"
        if type == "int":
            self.llvm += " i32 " + value +", align 4"
        return currentNode

    def VisitAssignment(self, currentNode):
        print("Assignment2LLVM")
        value = currentNode.rvalue.accept(self)
        currentNode.lvalue.acceptWithValue(self, value)
        return currentNode

