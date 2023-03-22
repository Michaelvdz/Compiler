import copy

from AST import *
import graphviz
from colorama import Fore

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class CreateSymbolTableVisitor(Visitor):

    def __init__(self, table):
        self.table = table

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
        print("Binary")
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
        return currentNode

    def VisitDeclaration(self, currentNode):
        print("Declaration")
        print(currentNode.var.value)
        print(currentNode.type.value)
        if not self.table.lookup(currentNode.var.name) is 0:
            self.table.insert(currentNode.var.value, currentNode.type.value)
        else:
            self.table.insert(currentNode.var.value, currentNode.type.value)
        
        if self.table.lookup(currentNode.var.value) is not 0:
            print("\n" + Fore.RED + "[ERROR]" + Fore.RESET + " variable " + currentNode.var.value + " has already been declared! \n")
        
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitAssignment(self, currentNode):
        print("Assignment")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode


