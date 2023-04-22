import copy

from AST import *
from SymbolTable import *
import graphviz
from colorama import Fore

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class CreateSymbolTableVisitor(Visitor):

    def __init__(self, table):
        self.table = table
        self.lineNr = 0
        self.positionNr = 0
        self.scopeNr = 0
        #print("----------------Creating Symbol Table----------------")
        globaltable = SymbolTable()
        globaltable.name = "Global"
        self.table.push(globaltable)

    def VisitASTNode(self, currentNode):
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitConditional(self, currentNode):
        #print("Scope")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitScope(self, currentNode):
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitWhile(self, currentNode):
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitFunction(self, currentNode):
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitExprLoop(self, currentNode):
        #print("Binary")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode
    def VisitBinaryOperation(self, currentNode):
        #print("Binary")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode
    def VisitUnaryOperation(self, currentNode):
        #print("Unary")
        for child in currentNode.children:
            node = child.accept(self)
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
        return currentNode

    def VisitJump(self, currentNode):
        #print("Jump")
        return currentNode

    def VisitDeclaration(self, currentNode):
        #print("Declaration")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitPointer(self, currentNode):
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitAssignment(self, currentNode):
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitVariable(self, currentNode):
        #print("Variable")
        return currentNode

    def VisitCall(self, currentNode):
        #print("Call")
        return currentNode

    def VisitMLComment(self, currentNode):
        #print("MLComment")
        return currentNode
    def VisitSLComment(self, currentNode):
        #print("SLComment")
        return currentNode
    def VisitPrintf(self, currentNode):
        #print("Printf")
        return currentNode
