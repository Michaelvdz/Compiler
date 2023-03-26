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
        if len(self.table.vars[currentNode.varName]) == 3:
            if len(currentNode.varType) == 0 and len(self.table.vars[currentNode.varName][0]) == 0:
                self.table.vars[currentNode.varName][2] = currentNode.value
        else:
            self.table.vars[currentNode.varName].append(currentNode.value)    
        return currentNode

    def VisitDeclaration(self, currentNode):
        print("Declaration")
        print(currentNode.var.value)
        print(currentNode.type.name)

        currConst = ""
        currType = ""

        if currentNode.type.name == "VariableType":
            currConst = currentNode.type.children[0].name
            currType = currentNode.type.children[1].name
        else:
            currType = currentNode.type.name

        # int i = 3;
        # int i = 7; Redeclaration
        if self.table.lookup(currentNode.var.value) != 0 and len(currType) != 0:
            print(
                "\n" + Fore.RED + "[ERROR]" + Fore.RESET + " variable " + currentNode.var.value + " has already been declared! \n")

        # int i = 3;
        # k = 7; Undefined variable
        if self.table.lookup(currentNode.var.value) == 0 and len(currType) == 0:
            print(
                "\n" + Fore.RED + "[ERROR]" + Fore.RESET + " variable " + currentNode.var.value + " has not been declared yet! \n")

        # const int i = 4;
        # i = 5; const can't be changed
        if self.table.lookup(currentNode.var.value) != 0 and len(currType) == 0:
            if self.table.lookup(currentNode.var.value)[0] == "const":
                print(
                    "\n" + Fore.RED + "[ERROR]" + Fore.RESET + " variable " + currentNode.var.value + " can not be changed because it's a const! \n")

        if self.table.lookup(currentNode.var.name) == 0 and len(currType) != 0:
            self.table.insert(currentNode.var.value, currConst, currType)

        for child in currentNode.children:
            node = child.accept(self)
        return currentNode
    
    def VisitAssignment(self, currentNode):
        print("Assignment")
        varName = currentNode.children[0].var.value
        varType = currentNode.children[0].type.name
        for child in currentNode.children:
            if child.name == "Constant":
                child.varName = varName
                child.varType = varType
                node = child.accept(self)
            else:
                node = child.accept(self)
        
        #check if a variable in the rvalue has been declared
        l = list()
        newL = [currentNode.children[1]]
        ok = True
        while ok:
            ok = False
            for i in newL:
                if i.name == i.value:
                    l.append(i.value)
                else:
                    if i.name != "Constant":
                        newL = i.children
                        ok = True

        for i in l:
            if self.table.lookup(i) == 0:
                print("\n" + Fore.RED + "[ERROR]" + Fore.RESET + " variable " + i + " has not been declared yet! \n")
        
        return currentNode


