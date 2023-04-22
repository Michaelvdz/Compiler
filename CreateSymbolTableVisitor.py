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
        #print("Node")
        if currentNode.children:
            if currentNode.children[0].name == "Comment":
                for i in range(currentNode.children[0].value.count('\n')):
                    self.lineNr += 1
        
        if currentNode.name == "Inst":
            self.lineNr += 1

        if len(currentNode.children) == 0 and currentNode.value != "Inst":
            if self.table.peek().lookup(currentNode.value) == 0:
                print("\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line "+ str(self.lineNr) + ": variable " + currentNode.value + " has not been declared yet! \n")

        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitConditional(self, currentNode):
        #print("Scope")
        # Creating Symbol Table for condition
        newtable = SymbolTable()
        newtable.name = currentNode.value
        # Get current ST als parent table
        parenttable = self.table.peek()
        newtable.parent = parenttable
        # Append new ST as child of parent ST
        parenttable.children.append(newtable)
        # Push ST to stack
        self.table.push(newtable)
        currentNode.ifbody.accept(self)
        # Pop after runthrough
        self.table.pop()
        if currentNode.elsebody:
            # Creating Symbol Table for condition
            newtable = SymbolTable()
            newtable.name = currentNode.value
            # Get current ST als parent table
            parenttable = self.table.peek()
            newtable.parent = parenttable
            # Append new ST as child of parent ST
            parenttable.children.append(newtable)
            # Push ST to stack
            self.table.push(newtable)
            currentNode.elsebody.accept(self)
            # Pop after runthrough
            self.table.pop()
        return currentNode

    def VisitScope(self, currentNode):
        # Creating Symbol Table for scope
        newtable = SymbolTable()
        # Name scope
        newtable.name = "Scope " + str(self.scopeNr)
        self.scopeNr += 1
        # Get current ST als parent table
        parenttable = self.table.peek()
        newtable.parent = parenttable
        # Append new ST as child of parent ST
        parenttable.children.append(newtable)
        # Push ST to stack
        self.table.push(newtable)
        for child in currentNode.children:
            node = child.accept(self)
        # Pop after run through
        self.table.pop()
        return currentNode

    def VisitWhile(self, currentNode):
        #print("While")
        # Creating Symbol Table for while
        newtable = SymbolTable()
        # Name scope
        newtable.name = "While-loop"
        parenttable = self.table.peek()
        newtable.parent = parenttable
        # Append new ST as child of parent ST
        parenttable.children.append(newtable)
        # Push ST to stack
        self.table.push(newtable)
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
        # Pop after run through
        self.table.pop()
        return currentNode

    def VisitFunction(self, currentNode):
        #print("Function - Creating new ST for the function")
        if currentNode.hasbody:
            # Creating Symbol Table for function
            newtable = SymbolTable()
            # Name scope
            newtable.name = currentNode.value
            parenttable = self.table.peek()
            newtable.parent = parenttable
            # Append new ST as child of parent ST
            parenttable.children.append(newtable)
            # Push ST to stack
            self.table.push(newtable)
            if currentNode.body:
                # if it has params, visit them
                for param in currentNode.params:
                    node = param.accept(self)
                # Visit body
                if currentNode.body:
                    currentNode.body.accept(self)
            # Pop after run through
            self.table.pop()
            # Add function to ST
            self.table.peek().insertFunction(currentNode.value, "", currentNode.returnType.value, "func")
        else:
            for param in currentNode.params:
                print(param.type)
            self.table.peek().insertFunction(currentNode.value, "", currentNode.returnType.value, "func")
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

        currConst = ""
        currType = ""


        if currentNode.type != "int" and currentNode.type != "float" and currentNode.type != "char" and currentNode.type != "char*"\
                and currentNode.type != "int*" and currentNode.type != "float*":
            currentNode.type = ""


        if currentNode.type == "VariableType":
            #print("dees?")
            currConst = currentNode.type.children[0].name
            currType = currentNode.type.children[1].name
        else:
            #print("nee dit!")
            currType = currentNode.type
            #print(currType)

        # int i = 3;
        # int i = 7; Redeclaration
        if self.table.peek().lookup(currentNode.var) != 0 and len(currType) != 0:
            print(
                "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(self.lineNr) + ": variable " + currentNode.var + " has already been declared! \n")

        # int i = 3;
        # k = 7; Undefined variable
        if self.table.peek().lookup(currentNode.var) == 0 and len(currType) == 0:
            print(
                "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(self.lineNr) + ": variable " + currentNode.var + " has not been declared yet! \n")

        # const int i = 4;
        # i = 5; const can't be changed
        if self.table.peek().lookup(currentNode.var) != 0 and len(currType) == 0:
            if self.table.peek().vars[currentNode.var].attr == "const":
                print(
                    "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(self.lineNr) + ": variable " + currentNode.var + " can not be changed because it's a const! \n")

        if self.table.peek().lookup(currentNode.var) == 0 and len(currType) != 0:
            # self.table.peek().insert(currentNode.var, currConst, currType, currentNode.attr)
            '''none'''

        print(currentNode.pointer)
        print(currentNode.var)
        if currentNode.pointer:
            node = currentNode.pointer.accept(self)
            for star in node.children:
                currType = currType + "*"
            currType += "*"
        print("Type of var")
        print(currType)




        if not self.table.peek().lookupInThisTable(currentNode.var):
            self.table.peek().insert(currentNode.var, currConst, currType, currentNode.attr)

        #currentNode.print()
        return currentNode

    def VisitPointer(self, currentNode):
        if currentNode.children:
            for child in currentNode.children:
                node = child.accept(self)
                for child2 in node.children:
                    currentNode.children.append(node)
                    node.children = []
                return currentNode
        else:
            return currentNode

    def VisitAssignment(self, currentNode):
        if isinstance(currentNode.lvalue, Variable):
            '''
            varName = currentNode.lvalue.var
            varType = currentNode.lvalue.type
            varAttr = currentNode.lvalue.attr

            #print(varType)
            lvalue = currentNode.lvalue
            #print(lvalue.type)
            lvalue.accept(self)

            rvalue = currentNode.rvalue
            rvalue.accept(self)
            '''
        else:
            currentNode.lvalue.accept(self)

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
