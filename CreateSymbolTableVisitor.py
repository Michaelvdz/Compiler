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
        globaltable.children = []
        globaltable.name = "Global"
        self.table.push(globaltable)

    def VisitASTNode(self, currentNode):
        #print("Node")
        if currentNode.children:
            '''
            if currentNode.children[0].name == "Comment":
                for i in range(currentNode.children[0].value.count('\n')):
                    self.lineNr += 1
            if currentNode.children[0].name == "return":
                print("\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                    self.lineNr) + ": return has not been used in a function! \n")
            '''
        '''
        if currentNode.name == "Inst":
            self.lineNr += 1
        
        if len(currentNode.children) == 0 and currentNode.value != "Inst":
            if self.table.peek().lookup(currentNode.value) == 0:
                print("\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line "+ str(self.lineNr) + ": variable " + currentNode.value + " has not been declared yet! \n")
        '''
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitInclude(self, currentNode):
        return currentNode
    def VisitConditional(self, currentNode):
        #print("Scope")
        # Creating Symbol Table for condition
        newtable = SymbolTable()
        newtable.name = currentNode.value+" if-scope"
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
            newtable.name = currentNode.value+" else-scope"
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
        returnType = currentNode.returnType.value
        if not currentNode.hasbody:
            '''
            if self.table.search(currentNode.value)[0]:
                if returnType != self.table.search(currentNode.value)[2]:
                    print(
                        "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                            self.lineNr) + ": function returnType does not match the original functions returnType! \n")
                else:
                    if len(currentNode.params) != self.table.search(currentNode.value)[1]:
                        print(
                            "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                                self.lineNr) + ": function parameters does not match the original functions parameters! \n")
            '''

        if currentNode.hasbody:
            '''
            if self.table.search(currentNode.value)[0]:
                print(
                    "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                        self.lineNr) + ": function name " + currentNode.value + " has already been used! \n")

            if currentNode.body is not None:
                if currentNode.body.children[-1].value != "return" and returnType != "void":
                    print(
                        "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                            self.lineNr) + ": function " + currentNode.value + " has no return at the end! \n")

                if currentNode.body.children[-1].value == "return" and returnType == "void":
                    print(
                        "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                            self.lineNr) + ": you can't use return in a void function \n")
            '''
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
            # if it has params, visit them
            #print("PPPPPPPPPPPPPPPP")
            #print(currentNode.params)
            parms = []
            for param in currentNode.params:
                #print("Param:")
                #print(param)
                node = param.accept(self)
                if node.pointer:
                    parms.append(node.type+"*")
                else:
                    parms.append(node.type)

            #print(parms)


            if currentNode.body:
                # Visit body
                if currentNode.body:
                    currentNode.body.accept(self)
            # Pop after run through
            self.table.pop()
            # Add function to ST
            symbol = self.table.peek().lookupUnallocated(currentNode.value)
            if not symbol:
                table = self.table.peek().insertFunction(currentNode.totalParams, currentNode.value, "", currentNode.returnType.value, "func")
                table.params = parms
        else:
            params = []
            for param in currentNode.params:
                #print(param.type)
                params.append(param.type)
            symbol = self.table.peek().lookupUnallocated(currentNode.value)
            #print("Symbol exists?")
            #print(symbol)
            if not symbol:
                table = self.table.peek().insertFunction(currentNode.totalParams, currentNode.value, "", currentNode.returnType.value, "func")
                table.params = params
        return currentNode

    def VisitExprLoop(self, currentNode):
        #print("Binary")
        if currentNode.children[0].name == "Call":
            '''
            numberOfPar = len(currentNode.children[0].children)
            if not self.table.search(currentNode.children[0].value)[0]:
                print(
                    "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                        self.lineNr) + ": function " + currentNode.value + " has not been made! \n")
            else:
                numberOfPar2 = self.table.search(currentNode.children[0].value)[1]
                if numberOfPar != numberOfPar2:
                    print("\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                        self.lineNr) + ": function " + currentNode.value + " has more/less parameters then given! \n")
            '''

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




        if currentNode.type == "VariableType":
            #print("dees?")
            currConst = currentNode.type.children[0].name
            currType = currentNode.type.children[1].name
        else:
            #print("nee dit!")
            currType = currentNode.type
            #print(currType)


        if currentNode.pointer:
            node = currentNode.pointer.accept(self)
            for star in node.children:
                currType = currType + "*"
            currType += "*"


        if currentNode.array:
            array = currentNode.array.accept(self)
            if not self.table.peek().lookupInThisTable(currentNode.var):
                #print("Inserting array var")
                size = array.value
                self.table.peek().insertArray(currentNode.var, currConst, currType+"[]", currentNode.attr, size)

        if "[]" not in currentNode.type:
            if not self.table.peek().lookupInThisTable(currentNode.var):
                #print("Inserting var")
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
            currentNode.lvalue.accept(self)
            currentNode.rvalue.accept(self)
        else:
            currentNode.lvalue.accept(self)

        return currentNode

    def VisitArray(self, currentNode):
        #print("Variable")
        return currentNode

    def VisitArrayVariable(self, currentNode):
        #print("Variable")
        return currentNode

    def VisitVariable(self, currentNode):
        #print("Variable")
        currConst = ""
        currType = ""
        if currentNode.type == "VariableType":
            #print("dees?")
            currConst = currentNode.type.children[0].name
            currType = currentNode.type.children[1].name
        else:
            #print("nee dit!")
            currType = currentNode.type
            #print(currType)


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
    def VisitScanf(self, currentNode):
        #print("Printf")
        return currentNode
