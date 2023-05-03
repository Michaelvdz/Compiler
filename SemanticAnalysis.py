import copy

from AST import *
from SymbolTable import *
import graphviz
from colorama import Fore

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class SemanticAnalysisVisitor(Visitor):

    def __init__(self):
        self.lineNr = 0
        self.positionNr = 0
        self.scopeNr = 0
        globaltable = SymbolTable()
        globaltable.name = "Global"
        self.currentScope = globaltable
        self.functions = {}
        self.functionsWithoutBody = {}


    def VisitASTNode(self, currentNode):
        if currentNode.children:
            if currentNode.children[0].name == "return":
                print("\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                    self.lineNr) + ": return has not been used in a function! \n")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitConditional(self, currentNode):
        # Creating the scope for condition
        newtable = SymbolTable()
        newtable.name = currentNode.value
        # Get current scope als parent scope
        parenttable = self.currentScope
        newtable.parent = parenttable
        # Append new scope as child of parent scope
        parenttable.children.append(newtable)
        # Updating currentScope and functions
        self.currentScope = newtable
        self.functions[newtable.name] = newtable
        currentNode.ifbody.accept(self)
        if currentNode.elsebody:
            # Creating the scope for condition
            newtable = SymbolTable()
            newtable.name = currentNode.value
            # Get current scope als parent scope
            parenttable = self.currentScope
            newtable.parent = parenttable
            # Append new scope as child of parent scope
            parenttable.children.append(newtable)
            # Updating currentScope and functions
            self.currentScope = newtable
            self.functions[newtable.name] = newtable
            currentNode.elsebody.accept(self)
        if self.currentScope.parent:
            self.currentScope = self.currentScope.parent
        return currentNode

    def VisitScope(self, currentNode):
        # Creating Symbol Table for scope
        newtable = SymbolTable()
        # Name scope
        newtable.name = "Scope " + str(self.scopeNr)
        self.scopeNr += 1
        # Get current ST als parent table
        parenttable = self.currentScope
        newtable.parent = parenttable
        # Append new ST as child of parent ST
        parenttable.children.append(newtable)
        self.currentScope = newtable
        self.functions[newtable.name] = newtable
        for child in currentNode.children:
            node = child.accept(self)
        if self.currentScope.parent:
            self.currentScope = self.currentScope.parent
        return currentNode

    def VisitWhile(self, currentNode):
        # Creating scope for while
        newtable = SymbolTable()
        # Name scope
        newtable.name = "While-loop"
        parenttable = self.currentScope
        newtable.parent = parenttable
        # Append new scope as child of parent scope
        parenttable.children.append(newtable)
        # Updating currentScope and functions
        self.currentScope = newtable
        self.functions[newtable.name] = newtable
        # if it has for loop and before part
        if currentNode.beforeLoop:
            currentNode.beforeLoop.accept(self)
        # if it has for loop and before part
        if currentNode.afterLoop:
            currentNode.afterLoop.accept(self)
        # Visit condition
        currentNode.condition.accept(self)
        # Visit body
        currentNode.body.accept(self)
        if self.currentScope.parent:
            self.currentScope = self.currentScope.parent
        return currentNode

    def VisitFunction(self, currentNode):
        returnType = currentNode.returnType.value
        currentNode.totalParams = len(currentNode.params)
        if not currentNode.hasbody:
            if self.functionsWithoutBody.get(currentNode.name) is not None:
                if returnType != self.functionsWithoutBody.get(currentNode.name).returnType.value:
                    print(
                        "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                            self.lineNr) + ": function returnType does not match the original functions returnType! \n")
                if currentNode.totalParams != self.functionsWithoutBody.get(currentNode.name).totalParams:
                    print(
                        "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                            self.lineNr) + ": function parameters does not match the original functions parameters! \n")
            if self.functions.get(currentNode.name) is not None:
                if returnType != self.functions.get(currentNode.name).returnType.value:
                    print(
                        "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                            self.lineNr) + ": function returnType does not match the original functions returnType! \n")
                if currentNode.totalParams != self.functions.get(currentNode.name).totalParams:
                    print(
                        "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                            self.lineNr) + ": function parameters does not match the original functions parameters! \n")

            l = []
            if currentNode.totalParams > 1:
                for i in currentNode.params:
                    if i.var in l:
                        print(
                            "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                                self.lineNr) + ": variable " + i.var + " has already been declared! \n")
                    else:
                        l.append(i.var)

        if currentNode.hasbody:
            if currentNode.hasbody is not None and currentNode.name != "main":

                if self.functionsWithoutBody.get(currentNode.name) is not None:
                    if returnType != self.functionsWithoutBody.get(currentNode.name).returnType.value:
                        print(
                            "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                                self.lineNr) + ": function returnType does not match the original functions returnType! \n")
                    if currentNode.totalParams != self.functionsWithoutBody.get(currentNode.name).totalParams:
                        print(
                            "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                                self.lineNr) + ": function params does not match the original functions params! \n")

                if currentNode.body is not None:
                    if currentNode.body.children[-1].value != "return" and returnType != "void":
                        print(
                            "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                                self.lineNr) + ": function " + currentNode.value + " has no return at the end! \n")
                    if currentNode.body.children[-1].value == "return" and returnType == "void":
                        print(
                            "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                                self.lineNr) + ": you can't use return in a void function \n")
                else:
                    if returnType != "void":
                        print(
                            "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                                self.lineNr) + ": function " + currentNode.value + " has no return at the end! \n")

            if self.functions.get(currentNode.value):
                print(
                    "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                        self.lineNr) + ": function name " + currentNode.value + " has already been used! \n")
            # Creating scope for function
            newtable = SymbolTable()
            # Name scope
            newtable.name = currentNode.value
            newtable.returnType = currentNode.returnType.value
            parenttable = self.currentScope
            newtable.parent = parenttable
            # Append new scope as child of parent scope
            parenttable.children.append(newtable)
            # Updating currentScope and functions
            self.currentScope = newtable
            self.functions[currentNode.value] = currentNode
            if currentNode.body:
                # if it has params, visit them
                for param in currentNode.params:
                    print("Param:")
                    print(param)
                    node = param.accept(self)
                    print(node.value)
                # Visit body
                if currentNode.body:
                    currentNode.body.accept(self)
            if self.currentScope.parent:
                self.currentScope = self.currentScope.parent

        else:
            for param in currentNode.params:
                print(param.type)
            self.functionsWithoutBody[currentNode.value] = currentNode

        return currentNode

    def VisitExprLoop(self, currentNode):
        #print("Binary")
        for i in currentNode.children:
            if i.name == "Call":
                if len(i.children) != self.functions.get(i.value.split("()")[0]):
                    print("\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                        self.lineNr) + ": function " + currentNode.value + " has more/less parameters then given! \n")

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
        varName = currentNode.var

        if self.currentScope.lookupUnallocated(varName) != 0:
            print(
                "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                    self.lineNr) + ": variable " + currentNode.var + " has already been declared! \n")

        self.currentScope.insert(varName, currentNode.attr, currentNode.type)

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
        if self.currentScope.lookupUnallocated(currentNode.value) == 0:
            print(
                "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                    self.lineNr) + ": variable " + currentNode.value + " has not been declared yet! \n")
        elif self.currentScope.lookupUnallocated(currentNode.value) != 0 and self.currentScope.lookupUnallocated(currentNode.value).constant == "const":
            print(
                "\n" + Fore.BLUE + "[ERROR]" + Fore.RESET + "line " + str(
                    self.lineNr) + ": variable " + currentNode.value + " can not be changed because it's a const! \n")

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
    def VisitArrayVariable(self, currentNode):
        return currentNode

    def VisitArray(self, currentNode):
        return currentNode
