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
        print("----------------Creating Symbol Table----------------")

    def VisitASTNode(self, currentNode):
        print("Node")

        print(len(currentNode.children))
        if len(currentNode.children) == 0:
            if self.table.lookup(currentNode.value) == 0:
                print("\n" + Fore.RED + "[ERROR]" + Fore.RESET + " variable " + currentNode.value + " has not been declared yet! \n")

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
        """
        if len(self.table.vars[currentNode.varName]) == 3:
            if len(currentNode.varType) == 0 and len(self.table.vars[currentNode.varName][0]) == 0:
                self.table.vars[currentNode.varName][2] = currentNode.value
        else:
            self.table.vars[currentNode.varName].append(currentNode.value)
        """
        return currentNode

    def VisitDeclaration(self, currentNode):
        print("Declaration")

        currConst = ""
        currType = ""
        
        if currentNode.type != "int" and currentNode.type != "float" and currentNode.type != "char":
            currentNode.type = ""

        if currentNode.type == "VariableType":
            print("dees?")
            currConst = currentNode.type.children[0].name
            currType = currentNode.type.children[1].name
        else:
            print("nee dit!")
            currType = currentNode.type

        # int i = 3;
        # int i = 7; Redeclaration
        if self.table.lookup(currentNode.var) != 0 and len(currType) != 0:
            print(
                "\n" + Fore.RED + "[ERROR]" + Fore.RESET + " variable " + currentNode.var + " has already been declared! \n")

        # int i = 3;
        # k = 7; Undefined variable
        if self.table.lookup(currentNode.var) == 0 and len(currType) == 0:
            print(
                "\n" + Fore.RED + "[ERROR]" + Fore.RESET + " variable " + currentNode.var + " has not been declared yet! \n")

        # const int i = 4;
        # i = 5; const can't be changed
        if self.table.lookup(currentNode.var) != 0 and len(currType) == 0:
            if self.table.vars[currentNode.var].attr == "const":
                print(
                    "\n" + Fore.RED + "[ERROR]" + Fore.RESET + " variable " + currentNode.var.value + " can not be changed because it's a const! \n")

        if self.table.lookup(currentNode.var) == 0 and len(currType) != 0:
            self.table.insert(currentNode.var, currConst, currType, currentNode.attr)

        """
        for child in currentNode.children:
            node = child.accept(self)
        """
        return currentNode
    
    def VisitAssignment(self, currentNode):
        print("Assignment")
        varName = currentNode.lvalue.var
        varType = currentNode.lvalue.type
        varAttr = currentNode.lvalue.attr

        lvalue = currentNode.lvalue
        lvalue.accept(self)

        rvalue = currentNode.rvalue
        rvalue.accept(self)

        """
        for child in currentNode.children:
            if child.name == "Constant":
                child.varName = varName
                child.varType = varType
                node = child.accept(self)
            else:
                if child.name != child.value:
                    node = child.accept(self)
                
        # Check if the variable in the lvalue has the same datatypes as the variables in the rvalue
        for i in l:
            if self.table.vars[i][1] != self.table.vars[varName][1]:
                print(
                    "\n" + Fore.RED + "[ERROR]" + Fore.RESET + " variable " + i + " has not the same datatype as variable " + varName + "\n")
        """
        return currentNode

    def VisitMLComment(self, currentNode):
        print("MLComment")
        return currentNode
    def VisitSLComment(self, currentNode):
        print("SLComment")
        return currentNode
    def VisitPrintf(self, currentNode):
        print("Printf")
        return currentNode
