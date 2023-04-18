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
        #currentNode.print()
        if currentNode.children:
            if currentNode.children[0].name == "Comment":
                for i in range(currentNode.children[0].value.count('\n')):
                    self.lineNr += 1
        
        if currentNode.name == "Inst":
            self.lineNr += 1
        
        #print(len(currentNode.children))
        if len(currentNode.children) == 0 and currentNode.value is not "Inst":
            if self.table.peek().lookup(currentNode.value) == 0:
                print("\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line "+ str(self.lineNr) + ": variable " + currentNode.value + " has not been declared yet! \n")

        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitConditional(self, currentNode):
        #print("Scope")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitScope(self, currentNode):
        print("Scope - Creating new ST for the scope")
        newtable = SymbolTable()
        newtable.name = "Scope " + str(self.scopeNr)
        self.scopeNr += 1
        parenttable = self.table.peek()
        print("Parent with name")
        print(parenttable.name)
        print("Parent with #children: " + str(len(parenttable.children)))
        newtable.parent = parenttable
        print("Parent with #children: " + str(len(parenttable.children)))
        parenttable.children.append(newtable)
        print("Parent with #children: " + str(len(parenttable.children)))
        print("Table with #children " + str(len(newtable.children)))
        self.table.push(newtable)
        print("staring scope")
        for child in currentNode.children:
            node = child.accept(self)
        print("end scope")
        self.table.pop()
        return currentNode

    def VisitWhile(self, currentNode):
        print("While")
        newtable = SymbolTable()
        newtable.name = "While-loop"
        parenttable = self.table.peek()
        print("Parent with name")
        print(parenttable.name)
        print("Parent with #children: " + str(len(parenttable.children)))
        newtable.parent = parenttable
        print("Parent with #children: " + str(len(parenttable.children)))
        parenttable.children.append(newtable)
        print("Parent with #children: " + str(len(parenttable.children)))
        print("Newtable with name:")
        print(newtable.name)
        print("Table with #children " + str(len(newtable.children)))
        self.table.push(newtable)
        '''
        for child in currentNode.children:
            node = child.accept(self)
        '''
        if currentNode.beforeLoop:
            currentNode.beforeLoop.accept(self)
        if currentNode.afterLoop:
            currentNode.afterLoop.accept(self)

        currentNode.condition.accept(self)
        currentNode.body.accept(self)
        self.table.pop()
        return currentNode

    def VisitFunction(self, currentNode):
        #print("Binary")
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
        """
        if len(self.table.vars[currentNode.varName]) == 3:
            if len(currentNode.varType) == 0 and len(self.table.vars[currentNode.varName][0]) == 0:
                self.table.vars[currentNode.varName][2] = currentNode.value
        else:
            self.table.vars[currentNode.varName].append(currentNode.value)
        """
        return currentNode

    def VisitJump(self, currentNode):
        #print("Jump")
        return currentNode

    def VisitDeclaration(self, currentNode):
        #print("Declaration")

        currConst = ""
        currType = ""
        #print(currentNode.type)


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
            print("Hij wilt dit toevoegen:")
            print(currentNode.var)
            print(currConst)
            print(currType)
            print(currentNode.attr)
            self.table.peek().insert(currentNode.var, currConst, currType, currentNode.attr)
            self.table.peek().print()

        """
        for child in currentNode.children:
            node = child.accept(self)
        """
        #currentNode.print()
        return currentNode
    
    def VisitAssignment(self, currentNode):
        #print("Assignment")
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
        print("Variable")
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
