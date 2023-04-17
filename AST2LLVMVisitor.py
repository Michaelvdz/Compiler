from AST import *
import graphviz
from SymbolTable import *
import struct

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class AST2LLVMVisitor(Visitor):

    llvm = ""
    symbolTable = 0
    instr = 1
    intprinting = False
    floatprinting = False
    charprinting = False
    printing = False
    lvalue = True
    currentTable = 0

    def __init__(self, llvm="", symbolTable=SymbolTable()):
        #print("----------------Converting AST 2 LLVM IR----------------")
        self.llvm = llvm
        self.symbolTable = symbolTable
        self.currentTable = symbolTable
        self.allocateRegisters(self.currentTable)
        self.currentTable.print()

    def allocateRegister(self, table, name, var):
        type = var.type
        attr = var.attr
        match type:
            case "int":
                self.llvm += "%" + str(self.instr) + " = alloca i32, align 4\n"
                table.insertRegister(name, str(self.instr))
                self.instr += 1
            case "float":
                self.llvm += "%" + str(self.instr) + " = alloca float, align 4\n"
                table.insertRegister(name, str(self.instr))
                self.instr += 1
            case "char":
                self.llvm += "%" + str(self.instr) + " = alloca i8, align 1\n"
                table.insertRegister(name, str(self.instr))
                self.instr += 1
            case "int*":
                self.llvm += "%" + str(self.instr) + " = alloca i32*, align 8\n"
                table.insertRegister(name, str(self.instr))
                self.instr += 1
            case "float*":
                self.llvm += "%" + str(self.instr) + " = alloca float*, align 8\n"
                table.insertRegister(name, str(self.instr))
                self.instr += 1
            case "char*":
                self.llvm += "%" + str(self.instr) + " = alloca i8*, align 8\n"
                table.insertRegister(name, str(self.instr))
                self.instr += 1
            case other:
                x = "test"
                #print("Type not implemented or literal")

    def allocateRegisters(self, table):
        print("Allocating registers:")
        for key, value in table.vars.items():
            print(key)
            print(value)
            self.allocateRegister(table, key, value)

        for child in table.children:
            self.allocateRegisters(child)


    def VisitASTNode(self, currentNode):
        print("Node")
        if self.currentTable.lookup(currentNode.value):
            return (str(self.currentTable.lookup(currentNode.value).register), str(self.currentTable.lookup(currentNode.value).type), "reg")
        else:
            for child in currentNode.children:
                node = child.accept(self)
            return currentNode

    def VisitConditional(self, currentNode):
        print("Conditional")
        # Get the usefull nodes from AST
        cond = currentNode.condition
        ifbody = currentNode.ifbody
        elsebody = currentNode.elsebody

        # Visit condition to get code
        reg = cond.accept(self)

        # Assign a label to the if body
        iflabel = self.instr
        self.instr += 1





        # If else body then add the label to the break instruction
        if elsebody:
            self.llvm += "br i1 %" + str(reg[0]) + ", label %" + str(iflabel) + ", label %" + "ELSE" + str(id(currentNode)) + "\n"
        else:
            self.llvm += "br i1 %" + str(reg[0]) + ", label %" + str(iflabel) + ", label %" + "CONTINUE" + str(id(currentNode)) + "\n"

        # Add the label of the if body and visit the ifbody
        self.llvm += "\n"
        self.llvm += str(iflabel) + ":\n"
        ifbody.accept(self)
        self.llvm += "br label %" + "CONTINUE" + str(id(currentNode))  + "\n"

        # If else body then add the label and visit the else body
        if elsebody:
            # If it has else, label else body
            elselabel = self.instr
            self.instr += 1
            self.llvm = self.llvm.replace("ELSE" + str(id(currentNode)), str(elselabel))
            self.llvm += "\n"
            self.llvm += str(elselabel) + ":\n"
            elsebody.accept(self)
            self.llvm += "br label %" + "CONTINUE" + str(id(currentNode)) + "\n"

        # Add label to next instructions
        # Label the next instruction, so we can jump when ending if or else
        continuelabel = self.instr
        self.instr += 1
        self.llvm = self.llvm.replace("CONTINUE" + str(id(currentNode)), str(continuelabel))
        self.llvm += "\n"
        self.llvm += str(continuelabel) + ":\n"
        return currentNode

    def VisitScope(self, currentNode):
        #print("Scope")
        print("Opening scope " + currentNode.value )

        # Open a new scope by selecting the right symbol table
        parent = self.currentTable
        self.currentTable = self.currentTable.children[0]
        print("-----------------------------------")
        print(self.currentTable.name)
        print(currentNode.children[0].value)
        #self.currentTable.print()

        # Visit scope body
        for child in currentNode.children:
            node = child.accept(self)

        # After visiting scope, delete the symbol table
        self.currentTable.parent.children.remove(self.currentTable)
        self.currentTable = parent
        return currentNode

    def VisitWhile(self, currentNode):
        print("While")
        # Open a new scope by selecting the right symbol table
        parent = self.currentTable
        self.currentTable = self.currentTable.children[0]

        # Get corresponding nodes from AST
        condition = currentNode.condition
        body = currentNode.body
        beforeloop = currentNode.beforeLoop
        afterloop = currentNode.afterLoop

        # Label condition
        conditionlabel = self.instr
        self.instr +=1



        self.llvm += "br label %" + str(conditionlabel) + "\n"

        # Condition part
        self.llvm += "\n"
        self.llvm += str(conditionlabel) + ":\n"
        reg = condition.accept(self)
        # Label body
        bodylabel = self.instr
        self.instr += 1
        self.llvm += "br i1 %" + str(reg[0]) + ", label %" + str(bodylabel) + " , label %" + str(id(currentNode)) + "\n"

        # Body part
        self.llvm += "\n"
        self.llvm += str(bodylabel) + ":\n"
        body.accept(self)
        # Label continue
        continuelabel = self.instr
        self.instr += 1
        self.llvm += "br label %" + str(conditionlabel) + "\n"

        # Continue part
        self.llvm += "\n"
        self.llvm += str(continuelabel) + ":\n"
        self.llvm = self.llvm.replace(str(id(currentNode)), str(continuelabel))


        '''
        for child in currentNode.children:
            node = child.accept(self)
        '''
        # After visiting scope, delete the symbol table
        self.currentTable.parent.children.remove(self.currentTable)
        self.currentTable = parent
        return currentNode

    def VisitVariable(self, currentNode):
        print("Variable")
        # For lvalue's look for the register
        if self.lvalue:
            if self.currentTable.lookup(currentNode.value):
                return (str(self.currentTable.lookup(currentNode.value).register), str(self.currentTable.lookup(currentNode.value).type), "reg")
            else:
                return currentNode
        else:
            symbol = self.currentTable.lookup(currentNode.value)
            type = symbol.type
            if type == "int":
                self.llvm += "%" + str(self.instr) + " = load i32, i32* %" + str(
                    symbol.register) + ", align 4\n"
                self.instr += 1
            if type == "float":
                self.llvm += "%" + str(self.instr) + " = load float, float* %" + str(
                    symbol.register) + ", align 4\n"
                self.instr += 1
            if type == "char":
                self.llvm += "%" + str(self.instr) + " = load i8, i8* %" + str(
                    symbol.register) + ", align 1\n"
                self.instr += 1
            return (str(self.instr-1), type, "reg")


    def VisitBinaryOperation(self, currentNode):
        print("Binary-----------")
        BinType = None
        children = []
        self.lvalue = False

        for child in currentNode.children:
            if isinstance(child, Variable):
                newType = self.currentTable.lookup(child.value).type
                if BinType is None:
                    BinType = newType
                elif newType == "float":
                    BinType = newType
            elif isinstance(child, Constant):
                print("Constant")
            children.append(child)

        left = currentNode.children[0].accept(self)
        right = currentNode.children[1].accept(self)
        lefttype = ""
        righttype = ""
        if not isinstance(currentNode.children[0], Constant):
            var0 = self.currentTable.lookup(currentNode.children[0].value)
            lefttype = left[1]
            leftvalue = "%" + left[0]
        else:
            leftvalue = left[0]
        if not isinstance(currentNode.children[1], Constant):
            var1 = self.currentTable.lookup(currentNode.children[1].value)
            righttype = right[1]
            rightvalue = "%" + right[0]
        else:
            rightvalue = right[0]
        if lefttype == "float" or righttype == "float":
            BinType = "float"


        if BinType == "float":
            if lefttype == "int":
                self.llvm += "%" + str(self.instr) + " = sitofp i32 " + str(leftvalue) + " to float\n"
                leftvalue = "%" + str(self.instr)
                self.instr += 1
            elif righttype == "int":
                self.llvm += "%" + str(self.instr) + " = sitofp i32 " + str(rightvalue) + " to float\n"
                rightvalue = "%" + str(self.instr)
                self.instr += 1

        match currentNode.value:
            case "+":
                if BinType == "int":
                    self.llvm += "%" + str(self.instr) + " = add nsw i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    self.llvm += "%" + str(self.instr) + " = fadd float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
            case "-":
                if BinType == "int":
                    self.llvm += "%" + str(self.instr) + " = sub nsw i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    self.llvm += "%" + str(self.instr) + " = fsub float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
            case "*":
                if BinType == "int":
                    self.llvm += "%" + str(self.instr) + " = mul nsw i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    self.llvm += "%" + str(self.instr) + " = fmul float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
            case "/":
                if BinType == "int":
                    self.llvm += "%" + str(self.instr) + " = sdiv nsw i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                        self.llvm += "%" + str(self.instr) + " = fdiv float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
            case "%":
                if BinType == "int":
                    self.llvm += "%" + str(self.instr) + " = srem nsw i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    self.llvm += "%" + str(self.instr) + " = frem float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
            case "==":
                if BinType == "int":
                    self.llvm += "%" + str(self.instr) + " = icmp eq i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    self.llvm += "%" + str(self.instr) + " = fcmp oeq float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
                #self.llvm += "%" + str(self.instr) + " = zext i1 %" + str(self.instr-1) + " to i32 \n"
                #self.instr += 1
                BinType = "int"
            case "<":
                if BinType == "int":
                    self.llvm += "%" + str(self.instr) + " = icmp slt i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    self.llvm += "%" + str(self.instr) + " = fcmp olt float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
                #self.llvm += "%" + str(self.instr) + " = zext i1 %" + str(self.instr-1) + " to i32 \n"
                #self.instr += 1
                BinType = "int"
            case "<=":
                if BinType == "int":
                    self.llvm += "%" + str(self.instr) + " = icmp lte i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    self.llvm += "%" + str(self.instr) + " = fcmp ole float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
                #self.llvm += "%" + str(self.instr) + " = zext i1 %" + str(self.instr-1) + " to i32 \n"
                #self.instr += 1
                BinType = "int"
            case ">":
                if BinType == "int":
                    self.llvm += "%" + str(self.instr) + " = icmp sgt i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    self.llvm += "%" + str(self.instr) + " = fcmp ogt float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
                #self.llvm += "%" + str(self.instr) + " = zext i1 %" + str(self.instr-1) + " to i32 \n"
                #self.instr += 1
                BinType = "int"
            case ">=":
                if BinType == "int":
                    self.llvm += "%" + str(self.instr) + " = icmp sgt i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    self.llvm += "%" + str(self.instr) + " = fcmp oge float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
                #self.llvm += "%" + str(self.instr) + " = zext i1 %" + str(self.instr-1) + " to i32 \n"
                #self.instr += 1
                BinType = "int"
            case "!=":
                if BinType == "int":
                    self.llvm += "%" + str(self.instr) + " = icmp ne i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    self.llvm += "%" + str(self.instr) + " = fcmp one float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
                #self.llvm += "%" + str(self.instr) + " = zext i1 %" + str(self.instr-1) + " to i32 \n"
                #self.instr += 1
                BinType = "int"

        return (str(self.instr-1), BinType, "reg")

    def VisitUnaryOperation(self, currentNode):
        print("Unary")
        match currentNode.value:
            case "&":
                node = currentNode.children[0].accept(self)
                return node
            case "*":
                #node = currentNode.children[0].accept(self)
                for child in currentNode.children:
                    node = child.accept(self)
                    if isinstance(node, ASTNode):
                        match self.symbolTable.lookup(node.value).type:
                            case "int*":
                                self.llvm += "%" + str(self.instr) + " = load i32*, i32** %" + str(self.symbolTable.lookup(node.value).register) + ", align 8\n"
                                self.instr += 1
                                return "%"+self.symbolTable.lookup(node.value).register
                            case "float*":
                                self.llvm += "%" + str(self.instr) + " = load float*, float** %" + str(
                                    self.symbolTable.lookup(node.value).register) + ", align 8\n"
                                self.instr += 1
                                return "%" + self.symbolTable.lookup(node.value).register
                            case "char*":
                                self.llvm += "%" + str(self.instr) + " = load i8*, i8** %" + str(
                                    self.symbolTable.lookup(node.value).register) + ", align 8\n"
                                self.instr += 1
                                return "%" + self.symbolTable.lookup(node.value).register
                    else:
                        #type = self.symbolTable.lookupByRegister(node).type
                        var = child.value
                        match self.symbolTable.lookupByRegister(node[0]).type:
                            case "int*":
                                self.llvm += "%" + str(self.instr) + " = load i32*, i32** %" + str(self.symbolTable.lookup(var).register) + ", align 8\n"
                                self.instr += 1
                                return self.symbolTable.lookup(var).register
                            case "float*":
                                self.llvm += "%" + str(self.instr) + " = load float*, float** %" + str(
                                    self.symbolTable.lookup(var).register) + ", align 8\n"
                                self.instr += 1
                                return self.symbolTable.lookup(var).register
                            case "char*":
                                self.llvm += "%" + str(self.instr) + " = load i8*, i8** %" + str(
                                    self.symbolTable.lookup(var).register) + ", align 8\n"
                                self.instr += 1
                                return self.symbolTable.lookup(var).register
                        return node
            case other:
                print("not implemented yet")
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
        print("Constant")
        #self.llvm+= " "+currentNode.value
        return (currentNode.value, "", "value")

    def VisitDeclaration(self, currentNode):
        #print("Declaration2LLVM")
        var = currentNode.var
        type = currentNode.type
        attr = currentNode.attr
        '''
        match type:
            case "int":
                self.llvm += "%" + str(self.instr) + " = alloca i32, align 4\n"
                print("Current table:")
                print(self.currentTable.name)
                self.currentTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case "float":
                self.llvm += "%" + str(self.instr) + " = alloca float, align 4\n"
                self.currentTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case "char":
                self.llvm += "%" + str(self.instr) + " = alloca i8, align 1\n"
                self.currentTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case "int*":
                self.llvm += "%" + str(self.instr) + " = alloca i32*, align 8\n"
                self.currentTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case "float*":
                self.llvm += "%" + str(self.instr) + " = alloca float*, align 8\n"
                self.currentTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case "char*":
                self.llvm += "%" + str(self.instr) + " = alloca i8*, align 8\n"
                self.currentTable.insertRegister(var, str(self.instr))
                self.instr += 1
            case other:
                x = "test"
                #print("Type not implemented or literal")
            '''
        return currentNode

    def VisitAssignment(self, currentNode):
        #print("Assignment2LLVM")

        # Test if the left value is a declaration
        if isinstance(currentNode.lvalue, Declaration):
            currentNode.lvalue.accept(self)
            value = currentNode.rvalue.accept(self)
            self.lvalue = True
            ltype = self.currentTable.lookup(currentNode.lvalue.var).type
            print(ltype)
            print(value)
            if value[2] is not "reg":
                if ltype == "int":
                    try:
                        value = int(value[0])
                    except ValueError:
                        value = float(value[0])
                    if isinstance(value, float) or isinstance(value, int):
                        self.llvm += "store i32 " + str(value) + ", i32* %" + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 4\n"
                elif ltype == "float":
                    try:
                        value = float(value[0])
                    except ValueError:
                        print("failiure")
                    self.llvm += "store float " + str(value) + ", float* %" + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "char":
                    value = value[0].replace("'","")
                    self.llvm += "store i8 " + str(ord(value)) + ", i8* %" + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 1\n"
                elif ltype == "int*":
                    self.llvm += "store i32* %" + str(value) + ", i32** %" + self.currentTable.lookup(
                        currentNode.lvalue.var).register + ", align 8\n"
                elif ltype == "float*":
                    self.llvm += "store float* %" + str(value) + ", float** %" + self.currentTable.lookup(
                        currentNode.lvalue.var).register + ", align 8\n"
                elif ltype == "char*":
                    self.llvm += "store i8* %" + str(value) + ", i8** %" + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 8\n"
            else:
                if ltype == "int":
                    if value[1] == "float":
                        self.llvm += "%" + str(self.instr) + " = fptosi float %" + str(value[0]) + " to i32\n"
                        self.instr += 1
                    self.llvm += "store i32 %" + str(self.instr - 1) + ", i32* %" + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "float":
                    if value[1] == "int":
                        self.llvm += "%" + str(self.instr) + " = sitofp i32 %" + str(value[0]) + " to float\n"
                        self.instr += 1
                    self.llvm += "store float %" + str(self.instr - 1) + ", float* %" + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "char":
                    self.llvm += "store i8 %" + str(self.instr - 1) + ", i8* %" + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 1\n"
                else:
                    print("test")

        # The lvalue is no declaration but a variable
        elif isinstance(currentNode.lvalue, Variable):
            value = currentNode.rvalue.accept(self)
            self.lvalue = True
            reg = currentNode.lvalue.accept(self)
            #ltype = self.symbolTable.lookup(currentNode.lvalue.children[0].value).type
            ltype = self.currentTable.lookup(currentNode.lvalue.value).type
            #self.instr += 1
            if ltype == "int*":
                self.llvm += "store i32* %" + str(value[0]) + ", i32** %" + str(reg) + ", align 8\n"
            if ltype == "float*":
                self.llvm += "store float* %" + str(value[0]) + ", float** %" + str(reg) + ", align 8\n"
            if ltype == "char*":
                self.llvm += "store i8* %" + str(value[0]) + ", i8** %" + str(reg) + ", align 1\n"
            if value[2] is not "reg":
                if ltype == "int":
                    try:
                        value = int(value[0])
                    except ValueError:
                        value = float(value[0])
                    if isinstance(value, float) or isinstance(value, int):
                        self.llvm += "store i32 " + str(value) + ", i32* %" + self.currentTable.lookup(currentNode.lvalue.value).register + ", align 4\n"
                elif ltype == "float":
                    try:
                        value = float(value[0])
                    except ValueError:
                        print("failiure")
                    self.llvm += "store float " + str(value) + ", float* %" + self.currentTable.lookup(currentNode.lvalue.value).register + ", align 4\n"
                elif ltype == "char":
                    value = value.replace("'","")
                    self.llvm += "store i8 " + str(ord(value)) + ", i8* %" + self.currentTable.lookup(currentNode.lvalue.value).register + ", align 1\n"
            else:
                if ltype == "int":
                    self.llvm += "store i32 %" + str(value[0]) + ", i32* %" + reg[0] + ", align 4\n"
                elif ltype == "float":
                    self.llvm += "store float %" + str(value[0]) + ", float* %" + reg[0] + ", align 4\n"
                elif ltype == "char":
                    value = value.replace("'","")
                    self.llvm += "store i8 " + str(ord(value[0])) + ", i8* %" + reg[0] + ", align 1\n"
        else:
            # In this case the lvalue is a pointer dereference
            value = currentNode.rvalue.accept(self)
            self.lvalue = True
            reg = currentNode.lvalue.accept(self)
            var = self.symbolTable.lookupByRegister(reg)
            type = var.type
            if type == "int*":
                try:
                    value = int(value[0])
                except ValueError:
                    value = float(value[0])
                if isinstance(value, float) or isinstance(value, int):
                    self.llvm += "store i32 " + str(value) + ", i32* %" + str(self.instr-1) + ", align 4\n"
                    #self.symbolTable.replaceRegisters(reg, str(self.instr-1))
            if type == "float*":
                try:
                    value = float(value[0])
                except ValueError:
                    print("failiure")
                if isinstance(value, float) or isinstance(value, int):
                    self.llvm += "store float " + str(value) + ", float* %" + str(self.instr-1) + ", align 4\n"
                    #self.symbolTable.replaceRegisters(reg, str(self.instr-1))
            if type == "char*":
                value = value[0].replace("'", "")
                self.llvm += "store i8 " + str(ord(value[0])) + ", i8* %" + str(self.instr-1) + ", align 1\n"
        return currentNode

    def VisitMLComment(self, currentNode):
        #print("MLComment")
        comment = currentNode.value
        comment = comment.replace("/*",";")
        comment = comment.replace("*/", ";")
        comment = comment.replace("* ", "; ")
        self.llvm += comment + "\n"
        return currentNode

    def VisitSLComment(self, currentNode):
        #print("SLComment")
        comment = currentNode.value
        comment = comment.replace("//", ";")
        self.llvm += comment + "\n"
        return currentNode

    def VisitPrintf(self, currentNode):
        print("Printf")
        node = currentNode.children[0].accept(self)
        #symbol = self.symbolTable.lookup(node.value)
        symbol = 0
        if not isinstance(node, ASTNode):
            symbol = self.currentTable.lookupByRegister(node[0])

        if symbol:
            if not self.printing:
                self.llvm = "declare i32 @printf(i8* noundef, ...)\n" + self.llvm
            match symbol.type:
                case "int":
                    if not self.intprinting:
                        self.llvm = "@.int = private unnamed_addr constant [3 x i8] c" + "\"" + "%d" + "\\00" + "\", align 1\n"\
                                 + self.llvm
                        self.intprinting = True
                        self.printing = True

                    self.llvm += "%"+ str(self.instr) + " = load i32, i32* %" + str(symbol.register) + ", align 4\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                 "@.int, i64 0, i64 0), i32 noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
                case "float":
                    if not self.floatprinting:
                        self.llvm = "@.float = private unnamed_addr constant [3 x i8] c" + "\"" + "%f" + "\\00" + "\", align 1\n"\
                                     + self.llvm
                        self.floatprinting = True
                        self.printing = True

                    self.llvm += "%" + str(self.instr) + " = load float, float* %" + str(symbol.register) + ", align 4\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = fpext float %" + str(int(self.instr) - 1) + " to double\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                 "@.float, i64 0, i64 0), double noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
                case "char":
                    if not self.charprinting:
                        self.llvm = "@.char = private unnamed_addr constant [3 x i8] c" + "\"" + "%c" + "\\00" + "\", align 1\n"\
                                     + self.llvm
                        self.charprinting = True
                        self.printing = True

                    self.llvm += "%" + str(self.instr) + " = load i8, i8* %" + str(symbol.register) + ", align 4\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = sext i8 %" + str(int(self.instr) - 1) + " to i32\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                 "@.char, i64 0, i64 0), i32 noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
        else:
            if '\'' not in node.value:
                try:
                    value = int(node.value)
                except ValueError:
                    value = float(node.value)
                if isinstance(value, int):
                    if not self.printing:
                        self.llvm = "declare i32 @printf(i8* noundef, ...)\n" + self.llvm
                    if not self.intprinting:
                        self.llvm = "@.int = private unnamed_addr constant [3 x i8] c" + "\"" + "%d" + "\\00" + "\", align 1\n" \
                                    + self.llvm
                        self.intprinting = True
                        self.printing = True


                    self.llvm += "%" + str(self.instr) + " = alloca i32, align 4\n"
                    self.instr += 1
                    self.llvm += "store i32 " + str(node.value) + ", i32* %" + str(self.instr - 1) + ", align 4\n"
                    self.llvm += "%" + str(self.instr) + " = load i32, i32* %" + str(self.instr - 1) + ", align 4\n"
                    self.instr += 1
                    self.llvm += "%" + str(
                        self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                      "@.int, i64 0, i64 0), i32 noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
                elif isinstance(value, float):
                    if not self.printing:
                        self.llvm = "declare i32 @printf(i8* noundef, ...)\n" + self.llvm
                    if not self.floatprinting:
                        self.llvm = "@.float = private unnamed_addr constant [3 x i8] c" + "\"" + "%f" + "\\00" + "\", align 1\n" \
                                    + self.llvm
                        self.charprinting = True
                        self.printing = True

                    self.llvm += "%" + str(self.instr) + " = alloca float, align 4\n"
                    self.instr += 1
                    self.llvm += "store float " + str(node.value) + ", float* %" + str(self.instr - 1) + ", align 4\n"
                    self.llvm += "%" + str(self.instr) + " = load float, float* %" + str(self.instr - 1) + ", align 4\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = fpext float %" + str(int(self.instr) - 1) + " to double\n"
                    self.instr += 1
                    self.llvm += "%" + str(
                        self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                      "@.float, i64 0, i64 0), double noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
            else:
                value = node.value.replace("'", "")
                if not self.printing:
                    self.llvm = "declare i32 @printf(i8* noundef, ...)\n" + self.llvm
                if not self.charprinting:
                    self.llvm = "@.char = private unnamed_addr constant [3 x i8] c" + "\"" + "%c" + "\\00" + "\", align 1\n" \
                                + self.llvm
                    self.charprinting = True
                    self.printing = True

                self.llvm += "%" + str(self.instr) + " = alloca i8, align 4\n"
                self.instr += 1
                self.llvm += "store i8 " + str(ord(value)) + ", i8* %" + str(self.instr - 1) + ", align 4\n"
                self.llvm += "%" + str(self.instr) + " = load i8, i8* %" + str(self.instr - 1) + ", align 4\n"
                self.instr += 1
                self.llvm += "%" + str(self.instr) + " = sext i8 %" + str(int(self.instr) - 1) + " to i32\n"
                self.instr += 1
                self.llvm += "%" + str(
                    self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                  "@.char, i64 0, i64 0), i32 noundef %" + str(int(self.instr) - 1) + ")\n"
                self.instr += 1
        return currentNode


