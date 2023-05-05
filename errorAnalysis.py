import copy
import re

from AST import *
from SymbolTable import *
import graphviz
from colorama import Fore


class Visitor:
    def __str__(self):
        return self.__class__.__name__


class Context:

    def __init__(self):
        self.vars = []


class errorAnalyser(Visitor):

    def __init__(self, table):
        self.table = table
        self.lineNr = 0
        self.positionNr = 0
        self.scopeNr = 0
        #print("----------------Performing semantic analysis----------------")
        self.context = []
        self.currentTable = 0
        self.currentTable = self.table
        #print(self.currentTable)
        self.lvalue = False
        self.errors = 0
        self.warnings = 0
        self.include = False
        main = self.currentTable.lookupAnalysis("main")
        if main == 0:
            print(
                "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                    self.lineNr) + ": main function not found \n")
            self.errors += 1

    def VisitASTNode(self, currentNode):
        # print("Node")
        '''
        if currentNode.children:
            if currentNode.children[0].name == "Comment":
                for i in range(currentNode.children[0].value.count('\n')):
                    self.lineNr += 1
            if currentNode.children[0].name == "return":
                print("\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                    self.lineNr) + ": return has not been used in a function! \n")

        if currentNode.name == "Inst":
            self.lineNr += 1

        if len(currentNode.children) == 0 and currentNode.value != "Inst":
            if self.table.peek().lookup(currentNode.value) == 0:
                print("\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                    self.lineNr) + ": variable " + currentNode.value + " has not been declared yet! \n")

        '''
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitInclude(self, currentNode):
        #print(currentNode.value)
        file = re.findall("<(.*)>", currentNode.value)
        if file[0] != "stdio.h":
            print(
                "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                    self.lineNr) + ": file not found '" + file[0] + "'\n")
            self.errors += 1
        else:
            self.include = True
        return currentNode

    def VisitConditional(self, currentNode):
        # print("Scope")
        table = self.currentTable.nextTable()
        if not table is self.currentTable:
            self.currentTable = table

        currentNode.ifbody.accept(self)
        self.currentTable.analysisDone = True
        self.currentTable = self.currentTable.parent
        if currentNode.elsebody:
            table = self.currentTable.nextTable()
            if not table is self.currentTable:
                self.currentTable = table

            currentNode.elsebody.accept(self)

            self.currentTable.analysisDone = True
            self.currentTable = self.currentTable.parent
        return currentNode

    def VisitScope(self, currentNode):
        # Creating Symbol Table for scope
        table = self.currentTable.nextTable()
        if not table is self.currentTable:
            self.currentTable = table

        for child in currentNode.children:
            node = child.accept(self)

        self.currentTable.analysisDone = True
        self.currentTable = self.currentTable.parent
        return currentNode

    def VisitWhile(self, currentNode):
        # print("While")
        table = self.currentTable.nextTable()
        if not table is self.currentTable:
            self.currentTable = table

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

        self.currentTable.analysisDone = True
        self.currentTable = self.currentTable.parent
        return currentNode

    def VisitFunction(self, currentNode):
        #print("We are in function")
        '''
        print("Function - Creating new ST for the function")
        returnType = currentNode.returnType.value
        if not currentNode.hasbody:
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
            #print("Hasbody")
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

            name = currentNode.value
            returnType = currentNode.returnType.value
            params = currentNode.params
            symbol = self.currentTable.lookupAnalysis(name)
            #print(symbol)
            #print(returnType)

            if symbol.defined == True:
                print(
                    "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                        self.lineNr) + ": function redefinition is not allowed '" + name + "'\n")
                self.errors += 1

            if self.currentTable.name != "Global":
                print(
                    "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                        self.lineNr) + ": function definition is not allowed in local scope '" + name + "'\n")
                self.errors += 1
            if symbol:
                if returnType != symbol.type:
                    print(
                        "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                            self.lineNr) + ": conflicting return types for definition of '" + name + "' '" + returnType + "' and '" + symbol.type + "'\n")
                    self.errors += 1

            if len(params) != len(symbol.params):
                print(
                    "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                        self.lineNr) + ": conflicting amount of parameter of '" + name + "' '" + str(
                        len(params)) + "' and '" + str(len(symbol.params)) + "'\n")
                self.errors += 1
            else:
                i = 0
                test = []
                for param in currentNode.params:
                    par = symbol.params.pop()
                    parmType = self.getType(param)
                    if parmType != par:
                        print(
                            "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                                self.lineNr) + ": conflicting parameter types for declaration of '" + name + "' '" + parmType + "' and '" + par + "'\n")
                        self.errors += 1
                    symbol.params.insert(i, par)
                    i += 1
            symbol.defined = True

            table = self.currentTable.nextTable()
            if not table is self.currentTable:
                self.currentTable = table

                if currentNode.body:
                    # if it has params, visit them
                    for param in currentNode.params:
                        node = param.accept(self)
                    # Visit body
                    if currentNode.body:
                        currentNode.body.accept(self)

            self.currentTable.analysisDone = True
            self.currentTable = self.currentTable.parent
        else:
            #print("The function is a declaration")
            name = currentNode.value
            returnType = currentNode.returnType.value
            params = currentNode.params
            symbol = self.currentTable.lookupAnalysis(name)

            #print(symbol)
            #print("Is declared?")
            #print(symbol.declared)

            if symbol.declared:
                if symbol:
                    if returnType != symbol.type:
                        print(
                            "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                                self.lineNr) + ": conflicting return types for declaration of '" + name + "' '" + returnType + "' and '" + symbol.type + "'\n")
                        self.errors += 1

                if len(params) != len(symbol.params):
                    print(
                        "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                            self.lineNr) + ": conflicting amount of parameter of '" + name + "' '" + str(len(params)) + "' and '" + str(len(symbol.params)) + "'\n")
                    self.errors += 1
                else:
                    i = 0
                    for param in currentNode.params:
                        par = symbol.params.pop()
                        if param.type != par:
                            print(
                                "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                                    self.lineNr) + ": conflicting parameter types for declaration of '" + name + "' '" + param.type + "' and '" + par + "'\n")
                            self.errors += 1
                        symbol.params.insert(i, par)
                        i += 1
            else:
                parameters = []
                for param in currentNode.params:
                    if isinstance(param, Declaration):
                        if param.var in parameters:
                            print(
                                "\n" + Fore.RED + "[ERROR]" + Fore.RESET + "line " + str(
                                    self.lineNr) + ": parameter redefinition in function '" + name + "', parameter '" + param.var + "'\n")
                            self.errors += 1
                        else:
                            parameters.append(param.var)
            symbol.declared = True


        return currentNode

    def VisitExprLoop(self, currentNode):
        # print("Binary")
        '''
        if currentNode.children[0].name == "Call":
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
        operator = currentNode.value
        type1 = self.getType(currentNode.children[0])
        type2 = self.getType(currentNode.children[1])
        #print(currentNode.children[0])
        #print(type1)
        #print(currentNode.children[1])
        #print(type2)
        if type1 == None or type2 == None:
            if type2 == None:
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": use of undeclared identifier '" + currentNode.children[1].value + "'\n")
                self.errors += 1
            if type1 == None:
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": use of undeclared identifier '" + currentNode.children[0].value + "'\n")
                self.errors += 1
        else:
            if (("[]" in type1) and isinstance(currentNode.children[0], Variable)) or ("[]" in type2 and isinstance(currentNode.children[1], Variable)):
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": invalid operands(array) to binary expression: \n")
                self.errors += 1
            else:
                if (type1 != type2) and ((type2 != "Unknown") and (type1 != "Unknown")):
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": operation of incompatible types: " + str(type1) + " and " + str(type2) + "\n")
                    self.errors += 1
                else:
                    currentNode.type = currentNode.children[0].type
            #print("Ending Binary")
        return currentNode

    def getType(self, var):
        #print(var.value)
        if isinstance(var, Constant):
            if var.type == "":
                value = var.value
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        value = value
                if isinstance(value, int):
                    return "int"
                elif isinstance(value, float):
                    return "float"
                else:
                    return "char"
            else:
                return var.type
        elif isinstance(var, Variable):
            #print(var.value)
            symbol = self.currentTable.lookupAnalysis(var.value)
            if symbol:
                return symbol.type
            else:
                return None
        elif isinstance(var, Call):
            symbol = self.currentTable.lookupAnalysis(var.value.replace("()",""))
            if symbol:
                return symbol.type
            else:
                return None
        elif isinstance(var, UnaryOperation):
            #print("We zijn hier")
            if var.value == "&":
                return "Address"
            elif var.value == "*":
                if not self.lvalue:
                    type = self.getPointerType(var)
                    return type.replace("*","")
                else:
                    symbol = self.currentTable.lookupAnalysis(var.value)
                    if symbol:
                        return symbol.type
                    else:
                        return None
            else:
                return self.getType(var.children[0])
        elif isinstance(var, ArrayVariable):
            symbol = self.currentTable.lookupAnalysis(var.value)
            if symbol:
                return symbol.type
            else:
                return None
        elif isinstance(var, Declaration):
            if var.pointer:
                return var.type + "*"
            else:
                return var.type
        elif isinstance(var, BinaryOperation):
            return "Unknown"

    def getPointerType(self, var):

        if var.value == "*":
            return self.getPointerType(var.children[0])
        else:
            return self.getType(var)

    def VisitUnaryOperation(self, currentNode):
        #print("Unary")
        if currentNode.value == "*":
            if isinstance(currentNode.children[0], Constant) or isinstance(currentNode.children[0], BinaryOperation):
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": Dereference requires pointer operand \n")
                self.errors += 1
        if currentNode.value == "&":
            if isinstance(currentNode.children[0], Constant) or isinstance(currentNode.children[0], BinaryOperation):
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": Cannot take the address of a literal\n")
                self.errors += 1
        if currentNode.value == "++" or currentNode.value == "--":
            if isinstance(currentNode.children[0], Constant):
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": invalid unary operation on literal\n")
                self.errors += 1
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitRelationOperation(self, currentNode):
        # print("Relation")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitLogicalOperation(self, currentNode):
        # print("Logical")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitConstant(self, currentNode):
        # print("Constant")
        return currentNode

    def VisitJump(self, currentNode):
        # print("Jump")
        if currentNode.value == "continue":
            if not self.currentTable.loopInScopes():
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": continue statement not in loop statement\n")
                self.errors += 1
        if currentNode.value == "break":
            if not self.currentTable.loopInScopes():
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": break statement not in loop statement\n")
                self.errors += 1
        if currentNode.value == "return":
            #print(self.currentTable.functionInScopes())
            if not self.currentTable.functionInScopes():
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": return statement not in function statement\n")
                self.errors += 1
        return currentNode

    def VisitDeclaration(self, currentNode):
        # print("Declaration")

        currConst = ""
        currType = ""

        if currentNode.type == "VariableType":
            #print("dees?")
            currConst = currentNode.type.children[0].name
            currType = currentNode.type.children[1].name
        else:
            #print("nee dit!")
            currType = currentNode.type



            symbol = self.currentTable.lookupAnalysis(currentNode.var)
            #print(symbol)

            if symbol.declared == True:

                if symbol.type == currType:
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": redefinition of '" + currentNode.var + "'\n")
                    self.errors += 1
                else:
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": redefinition of '" + currentNode.var + "' with a different type: '" + currType + "' vs '" + symbol.type + "'\n")
                    self.errors += 1
            else:
                if "[]" in symbol.type:
                    arraySizeType = self.getType(currentNode.array)
                    if arraySizeType != "int":
                        print(
                            "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                                self.lineNr) + ": size of array has non-integer type '" + arraySizeType + "'\n")
                        self.errors += 1
                    else:
                        symbol.declared = True
                symbol.declared = True
            # print(currType)

        '''
        if currentNode.pointer:
            node = currentNode.pointer.accept(self)
            for star in node.children:
                currType = currType + "*"
            currType += "*"

        if currentNode.array:
            array = currentNode.array.accept(self)
            if not self.table.peek().lookupInThisTable(currentNode.var):
                print("Inserting array var")
                size = array.value
        '''



        # currentNode.print()
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
            #print("Left side, no declaration")
            self.lvalue = True
            currentNode.lvalue.accept(self)
            type1 = self.getType(currentNode.lvalue)
            self.lvalue = False
            currentNode.rvalue.accept(self)
            type2 = self.getType(currentNode.rvalue)
            #print("Types")
            #print(type1)
            #print(type2)
            symbol = self.currentTable.lookupAnalysis(currentNode.lvalue.value)
            if type1 == None:
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": use of undeclared identifier '" + currentNode.lvalue.value + "'\n")
                self.errors += 1
            if type1 != None and (type2 != None or type2 != "Unknown"):
                if ("*" not in type1) and (type2 == "Address"):
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": Assignment of incompatible types: " + type1 + " and " + type2 + "\n")
                    self.errors += 1
                elif (type1 != type2) and (type1 == "int" and type2 == "float"):
                    print(
                        "\n" + Fore.MAGENTA + "[WARNING] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": Possible information loss: " + type2 + " conversion to " + type1 + "\n")
                    self.warnings += 1
                elif (type1 != type2) and (type1 == "char" and type2 == "int"):
                    print(
                        "\n" + Fore.MAGENTA + "[WARNING] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": Possible information loss: " + type2 + " conversion to " + type1 + "\n")
                    self.warnings += 1
                elif (("*" not in type1) and (type2 == "Address")) and (type1 != type2):
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": Assignment of incompatible types: " + type1 + " and " + type2 + "\n")
                    self.errors += 1
            if symbol:
                if symbol.attr == "const":
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": Cannot reassign constant: '" + currentNode.lvalue.value + "'\n")
                    self.errors += 1
        elif isinstance(currentNode.lvalue, Declaration):
            #print("leftside, declaration")
            self.lvalue = True
            symbol = self.currentTable.lookupAnalysis(currentNode.lvalue.var)
            self.lvalue = False
            type1 = symbol.type
            #print(type1)
            #print(symbol)
            if symbol.defined:
                if symbol.type == currentNode.lvalue.type:
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": redefinition of '" + currentNode.lvalue.var + "'\n")
                    self.errors += 1
                else:
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": redefinition of '" + currentNode.lvalue.var + "' with a different type: '" + currentNode.lvalue.type + "' vs '" + symbol.type + "'\n")
                    self.errors += 1
            else:
                symbol.defined = True
            currentNode.rvalue.accept(self)
            type2 = self.getType(currentNode.rvalue)
            #print(type2)
            if type1 == None:
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": use of undeclared identifier '" + currentNode.lvalue.value + "'\n")
                self.errors += 1
            if type1 != None and type2 != None:
                if ("*" not in type1) and (type2 == "Address"):
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": Assignment of incompatible types: " + type1 + " and " + type2 + "\n")
                    self.errors += 1
                elif (type1 != type2) and (type1 == "int" and type2 == "float"):
                    print(
                        "\n" + Fore.MAGENTA + "[WARNING] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": Possible information loss: " + type2 + " conversion to " + type1 + "\n")
                    self.warnings += 1
                elif (type1 != type2) and (type1 == "char" and type2 == "int"):
                    print(
                        "\n" + Fore.MAGENTA + "[WARNING] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": Possible information loss: " + type2 + " conversion to " + type1 + "\n")
                    self.warnings += 1
                elif (("*" not in type1) and (type2 == "Address")) and (type1 != type2):
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": Assignment of incompatible types: " + type1 + " and " + type2 + "\n")
                    self.errors += 1
        else:
            #print("Hier dan?")
            currentNode.lvalue.accept(self)

        return currentNode

    def VisitArray(self, currentNode):
        # print("Variable")
        return currentNode

    def VisitArrayVariable(self, currentNode):
        #print("ArrayVariable")
        indexType = self.getType(currentNode.index)
        #print(indexType)
        symbol = self.currentTable.lookupAnalysis(currentNode.value)
        #print(currentNode.value)
        #print(symbol)
        if "[]" not in symbol.type:
            print(
                "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                    self.lineNr) + ": subscripted value is not an array \n")
            self.errors += 1
        else:
            if indexType != "int" and indexType != "Unknown":
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": array index is not an integer \n")
                self.errors += 1

        return currentNode

    def VisitVariable(self, currentNode):
        # print("Variable")
        #print(currentNode.value)
        if not self.lvalue:
            symbol = self.currentTable.lookupAnalysis(currentNode.value)
            if not symbol:
                print(
                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                        self.lineNr) + ": use of undeclared identifier '" + currentNode.value + "'\n")
                self.errors += 1
        return currentNode

    def VisitCall(self, currentNode):
        #print("Call")
        symbol = self.currentTable.lookupAnalysis(currentNode.value.replace("()", ""))
        #print(symbol.params)
        if not symbol:
            print(
                "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                    self.lineNr) + ": undefined reference to function '" + currentNode.value + "'\n")
            self.errors += 1
        else:
            if len(currentNode.children) != len(symbol.params):
                if len(currentNode.children) < len(symbol.params):
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": too few arguments to function call '" + currentNode.value + "', expected '"+ str(len(symbol.params)) + "', have '" + str(len(currentNode.children)) + "'\n")
                    self.errors += 1
                if len(currentNode.children) > len(symbol.params):
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": too many arguments to function call '" + currentNode.value + "', expected '"+ str(len(symbol.params)) + "', have '" + str(len(currentNode.children)) + "'\n")
                    self.errors += 1
            else:
                if currentNode.children:
                    i = 0
                    for arg in currentNode.children:
                        type = self.getType(arg)
                        #print(arg)
                        #print("type")
                        #print(type)
                        paramtype = symbol.params[i]
                        if type.lower() == "address":
                            if (type != paramtype) and (("*" not in paramtype) and (type == "address")):
                                print(
                                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                                        self.lineNr) + ": incompatible types for function call '" + currentNode.value + "', expected '" + str(
                                        paramtype) + "', have '" + str(type) + "'\n")
                                self.errors += 1
                        else:
                            if (type != paramtype):
                                print(
                                    "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                                        self.lineNr) + ": incompatible types for function call '" + currentNode.value + "', expected '" + str(
                                        paramtype) + "', have '" + str(type) + "'\n")
                                self.errors += 1
                        i += 1

        return currentNode

    def VisitMLComment(self, currentNode):
        # print("MLComment")
        return currentNode

    def VisitSLComment(self, currentNode):
        # print("SLComment")
        return currentNode

    def VisitPrintf(self, currentNode):
        # print("Printf")
        #print("SEMANTIC ON PRINTING")
        if not self.include:
            print(
                "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                    self.lineNr) + ": stdio.h not included \n")
            self.errors += 1
            return currentNode
        else:
            format = currentNode.format.value
            args = [*re.findall("%[0-9]*d|%[0-9]*f|%[0-9]*s|%[0-9]*i|%[0-9]*c", format)]
            #print(len(args))
            #print(len(currentNode.children))
            #print(currentNode.args)
            if len(args) != len(currentNode.args):
                if len(args) > len(currentNode.args):
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": too few arguments to printf function call, expected '" + str(
                            len(args)) + "', have '" + str(len(currentNode.args)) + "'\n")
                    self.errors += 1
                if len(args) < len(currentNode.args):
                    print(
                        "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                            self.lineNr) + ": too many arguments to printf function call, expected '" + str(
                            len(args)) + "', have '" + str(len(currentNode.args)) + "'\n")
                    self.errors += 1
            #print(args)
            i = 0
            if len(args) == len(currentNode.args):
                for child in currentNode.args:
                    type = self.getType(child.accept(self))
                    if type != None:
                        if (type == "int") and (("s" in args[i]) or ("c" in args[i]) or ("f" in args[i])):
                            print(
                                "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                                    self.lineNr) + ": incompatible types for printf function call, expected '" + str(
                                    args[i]) + "', have '" + str(type) + "'\n")
                            self.errors += 1

                        if (type == "float") and (("s" in args[i]) or ("c" in args[i]) or ("i" in args[i]) or ("d" in args[i])):
                            print(
                                "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                                    self.lineNr) + ": incompatible types for printf function call, expected '" + str(
                                    args[i]) + "', have '" + str(type) + "'\n")
                            self.errors += 1
                        if (type == "char") and (("i" in args[i]) or ("d" in args[i]) or ("f" in args[i])):
                            print(
                                "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                                    self.lineNr) + ": incompatible types for printf function call, expected '" + str(
                                    args[i]) + "', have '" + str(type) + "'\n")
                            self.errors += 1
                    i += 1

        return currentNode

    def VisitString(self, currentNode):
        # print("Printf")
        return currentNode

    def VisitScanf(self, currentNode):
        # print("Printf")
        if not self.include:
            print(
                "\n" + Fore.RED + "[ERROR] " + Fore.RESET + "line " + str(
                    self.lineNr) + ": stdio.h not included \n")
            self.errors += 1
            return currentNode
        else:
            return currentNode
