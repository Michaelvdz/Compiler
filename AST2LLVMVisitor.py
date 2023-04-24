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
    instr = 0
    intprinting = False
    floatprinting = False
    charprinting = False
    printing = False
    scanning = False
    lvalue = True
    currentTable = 0
    currentLoop = []
    context = []
    printstr = []

    def __init__(self, llvm="", symbolTable=SymbolTable()):
        #print("----------------Converting AST 2 LLVM IR----------------")
        self.llvm = llvm
        self.symbolTable = symbolTable
        self.currentTable = symbolTable
        #self.allocateRegisters(self.currentTable)
        self.currentLoop = []
        #self.currentTable.print()

    def allocateRegister(self, table, name, var):
        type = var.type
        attr = var.attr
        if type == "int":
            self.llvm += "%" + str(self.instr) + " = alloca i32, align 4\n"
            table.insertRegister(name, str(self.instr))
            self.instr += 1
        elif type == "float":
            self.llvm += "%" + str(self.instr) + " = alloca float, align 4\n"
            table.insertRegister(name, str(self.instr))
            self.instr += 1
        elif type == "char":
            self.llvm += "%" + str(self.instr) + " = alloca i8, align 1\n"
            table.insertRegister(name, str(self.instr))
            self.instr += 1
        elif "int*" in type:
            llvmtyp = type.replace("int","i32")
            self.llvm += "%" + str(self.instr) + " = alloca " + str(llvmtyp) + ", align 8\n"
            table.insertRegister(name, str(self.instr))
            self.instr += 1
        elif "float*" in type:
            llvmtyp = type.replace("float", "float")
            self.llvm += "%" + str(self.instr) + " = alloca " + str(llvmtyp) + ", align 8\n"
            table.insertRegister(name, str(self.instr))
            self.instr += 1
        elif "char*" in type:
            llvmtyp = type.replace("char", "i8")
            self.llvm += "%" + str(self.instr) + " = alloca " + str(llvmtyp) + ", align 8\n"
            table.insertRegister(name, str(self.instr))
            self.instr += 1
        else:
            print("Type not implemented")

    def allocateRegisters(self, table):
        print("Allocating registers:")
        for key, value in table.vars.items():
            self.allocateRegister(table, key, value)

        for child in table.children:
            self.allocateRegisters(child)

    def allocateRegistersCurrentScope(self, table):
        print("Allocating registers:")
        i = 0
        for key, value in table.vars.items():
            self.allocateRegister(table, key, value)
            i += 1
        return i

    def VisitASTNode(self, currentNode):
        print("Node")
        if self.currentTable.lookup(currentNode.value):
            return (str(self.currentTable.lookup(currentNode.value).register), str(self.currentTable.lookup(currentNode.value).type), "reg")
        else:
            if len(currentNode.children) == 1:
                return currentNode.children[0].accept(self)
            for child in currentNode.children:
                node = child.accept(self)
            return currentNode

    def VisitExprLoop(self, currentNode):
        print("ExprLoop")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitCall(self, currentNode):
        print("VisitCall")
        print("Look for :")
        print(currentNode.value)
        params = []

        # Prepare arguments
        for child in currentNode.children:
            print(child)
            node = child.accept(self)
            print(node)
            # When the arg is reference and no value
            if isinstance(child, UnaryOperation):
                node = (node[0], node[1], node[2], node[3], "ref")
                params.append(node)
            # When the arg is a value
            elif node[2] == "reg":
                symbol = self.currentTable.lookup(node[3])
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
                newnode = (self.instr - 1, node[1], node[2], node[3], "value")
                params.append(newnode)
            else:
                print(node)
                params.append(node)
        print("#params")
        print(len(params))

        # Print function call
        func = self.currentTable.lookup(currentNode.value.replace("()",""))
        if func and func.attr == "func":
            if func.type == "int":
                self.llvm += "%" + str(self.instr) + " = call i32" + " @" + currentNode.value.replace("()","")
            elif func.type == "float":
                self.llvm += "%" + str(self.instr) + " = call float" + " @" + currentNode.value.replace("()","")
            elif func.type == "char":
                self.llvm += "%" + str(self.instr) + " = call i8" + " @" + currentNode.value.replace("()","")
            elif "int*" in func.type:
                functype = func.type.replace("int", "i32")
                self.llvm += "%" + str(self.instr) + " = call " + functype + " @" + currentNode.value.replace("()","")
            else:
                self.llvm += "call void" + " @" + currentNode.value.replace("()", "")
                self.instr -= 1
            self.llvm += "("
            print("Parameters:")
            i = 1
            numberParams = len(currentNode.children)
            for node in params:
                print(node)
                if node[2] == "reg" and node[4] == "value":
                    if node[1] == "int":
                        self.llvm += "i32 noundef %" + str(node[0])
                    elif node[1] == "float":
                        self.llvm += "float noundef %" + str(node[0])
                    else:
                        self.llvm += "i8 noundef %" + str(node[0])
                elif node[2] == "reg" and node[4] == "ref":
                    if "int" in node[1]:
                        self.llvm += "i32* noundef %" + str(node[0])
                    elif "float" in node[1]:
                        self.llvm += "float* noundef %" + str(node[0])
                    else:
                        self.llvm += "i8* noundef %" + str(node[0])
                elif node[2] == "value":
                    if node[1] == "int":
                        self.llvm += "i32 noundef " + str(node[0])
                    elif node[1] == "float":
                        self.llvm += "float noundef " + str(node[0])
                    else:
                        self.llvm += "i8 noundef " + str(node[0])

                if i != numberParams:
                    self.llvm += ", "
                i += 1
            self.llvm += ")"
            self.llvm += "\n"
            self.instr +=1
        return (self.instr-1, "", "reg")

    def VisitFunction(self, currentNode):
        print("Function")
        self.instr = 0
        hasreturn = len(self.context)
        if currentNode.hasbody:
            # Open a new scope by selecting the right symbol table
            parent = self.currentTable
            self.currentTable = self.currentTable.children[0]

            returntype = currentNode.returnType.value
            funcname = currentNode.value
            self.llvm += "define dso_local "
            if returntype == "int":
                self.llvm += "i32 "
            elif returntype == "float":
                self.llvm += "float "
            elif returntype == "char":
                self.llvm += "i8 "
            elif "int*" in returntype:
                returntype = returntype.replace("int", "i32")
                self.llvm += returntype + " "
            elif "float*" in returntype:
                returntype = returntype.replace("int", "i32")
                self.llvm += returntype + " "
            elif "char*" in returntype:
                returntype = returntype.replace("int", "i32")
                self.llvm += returntype + " "
            else:
                self.llvm += "void "
            self.llvm += "@" + funcname
            if currentNode.params:
                self.llvm += "("
                params = currentNode.params
                numberParams = len(params)
                i = 1
                for param in params:
                    param2 = self.currentTable.lookupInThisTable(param.var)
                    paramtype = param2.type
                    if paramtype == "int":
                        paramtype = "i32"
                    elif paramtype == "float":
                        paramtype = "float"
                    elif paramtype == "char":
                        paramtype = "i8"
                    elif "int*" in paramtype:
                        paramtype = paramtype.replace("int", "i32")
                        #self.llvm += paramtype + " "
                    elif "float*" in paramtype:
                        paramtype = paramtype.replace("int", "i32")
                        #self.llvm += paramtype + " "
                    elif "char*" in paramtype:
                        paramtype = paramtype.replace("int", "i32")
                        #self.llvm += paramtype + " "
                    self.llvm += paramtype + " noundef %" + str(self.instr)
                    if i != numberParams:
                        self.llvm += ", "
                    self.instr += 1
                    i += 1
                self.llvm += "){\n"
            else:
                self.llvm += "(){\n"
            self.instr += 1
            number = self.allocateRegistersCurrentScope(self.currentTable)
            instr = self.instr - (len(currentNode.params) + number + 1)
            if currentNode.params:
                params = currentNode.params
                for param in params:
                    param2 = self.currentTable.lookupInThisTable(param.var)
                    node = param.accept(self)
                    paramtype = param2.type
                    reg = self.currentTable.lookupInThisTable(node.var).register
                    if paramtype == "int":
                        self.llvm += "store i32 %" + str(instr) + " , i32* %" + str(reg) + ", align 4\n"
                    elif paramtype == "float":
                        self.llvm += "store float %" + str(instr) + " , float %" + str(reg) + ", align 4\n"
                    elif paramtype == "char":
                        self.llvm += "store i8 %" + str(instr) + " , i8* %" + str(reg) + ", align 1\n"
                    elif "int*" in paramtype:
                        print("PARAM TYPE:")
                        param = paramtype.replace("int", "i32")
                        print(param)
                        self.llvm += "store " + param + " %" + str(instr) + " , " + param + "* %" + str(reg) + ", align 4\n"
                    else:
                        print("None")
                    instr += 1

            if currentNode.body:
                node = currentNode.body.accept(self)
            newhasreturn = len(self.context)
            print("New #return in stack")
            print(newhasreturn)
            if newhasreturn != hasreturn + 1:
                self.llvm += "ret void\n"
            else:
                self.context.pop()
            # After visiting scope, delete the symbol table
            self.currentTable.parent.children.remove(self.currentTable)
            self.currentTable = parent
            self.llvm += "}\n"
        return currentNode

    def VisitJump(self, currentNode):
        print("Jump")
        if currentNode.value == "break":
            currentid = self.currentLoop.pop()
            self.llvm += "br label %" + "CONTINUE" + currentid[0] + "            ;break\n"
            self.llvm += "BREAK"
            self.currentLoop.append((currentid[0], "break"))
        elif currentNode.value == "continue":
            currentid = self.currentLoop.pop()
            self.llvm += "br label %" + "CONDITION" + currentid[0] + "            ;continue\n"
            self.llvm += "NEXTLOOP"
            self.currentLoop.append((currentid[0], "continue"))
        elif currentNode.value == "return":
            if currentNode.children:
                self.lvalue = False
                result = currentNode.children[0].accept(self)
                self.lvalue = True
                print(result)
            else:
                result = ("0", "", "value")
            if currentNode.type == "int":
                if result[2] == "reg":
                    reg = self.loadRegister(result[0])
                    self.llvm += "ret i32 %" + str(reg) + "\n"
                else:
                    self.llvm += "ret i32 " + str(result[0]) + "\n"
            if currentNode.type == "float":
                if result[2] == "reg":
                    reg = self.loadRegister(result[0])
                    self.llvm += "ret float %" + str(reg) + "\n"
                else:
                    self.llvm += "ret float " + str(result[0]) + "\n"
            if currentNode.type == "char":
                if result[2] == "reg":
                    reg = self.loadRegister(result[0])
                    self.llvm += "ret i8 %" + str(reg) + "\n"
                else:
                    self.llvm += "ret i8 " + str(result[0]) + "\n"
            if currentNode.type == "void":
                self.llvm += "ret void\n"
            self.context.append("return")
        return currentNode

    def loadRegister(self, register):
        symbol = self.currentTable.lookupByRegister(register)
        if symbol:
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
            return self.instr - 1
        return self.instr - 1

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

        # Open a new scope by selecting the right symbol table
        parent = self.currentTable
        self.currentTable = self.currentTable.children[0]
        self.allocateRegistersCurrentScope(self.currentTable)
        ifbody.accept(self)
        # After visiting scope, delete the symbol table
        self.currentTable.parent.children.remove(self.currentTable)
        self.currentTable = parent

        if "BREAK" in self.llvm:
            self.llvm = self.llvm[:(self.llvm.rfind("BREAK"))]
        elif "NEXTLOOP" in self.llvm:
            self.llvm = self.llvm[:(self.llvm.rfind("NEXTLOOP"))]
        else:
            self.llvm += "br label %" + "CONTINUE" + str(id(currentNode))  + "\n"

        # If else body then add the label and visit the else body
        if elsebody:
            # If it has else, label else body
            elselabel = self.instr
            self.instr += 1
            self.llvm = self.llvm.replace("ELSE" + str(id(currentNode)), str(elselabel))
            self.llvm += "\n"
            self.llvm += str(elselabel) + ":\n"

            # Open a new scope by selecting the right symbol table
            parent = self.currentTable
            self.currentTable = self.currentTable.children[0]
            elsebody.accept(self)
            # After visiting scope, delete the symbol table
            self.currentTable.parent.children.remove(self.currentTable)
            self.currentTable = parent

            if "BREAK" in self.llvm:
                self.llvm = self.llvm[:(self.llvm.rfind("BREAK"))]
            elif "NEXTLOOP" in self.llvm:
                self.llvm = self.llvm[:(self.llvm.rfind("NEXTLOOP"))]
            else:
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

        # Visit scope body
        for child in currentNode.children:
            node = child.accept(self)

        # After visiting scope, delete the symbol table
        self.currentTable.parent.children.remove(self.currentTable)
        self.currentTable = parent
        return currentNode

    def VisitWhile(self, currentNode):
        print("While")
        self.currentLoop.append((str(id(currentNode)), ""))

        # Open a new scope by selecting the right symbol table
        parent = self.currentTable
        self.currentTable = self.currentTable.children[0]

        self.allocateRegistersCurrentScope(self.currentTable)
        # Get corresponding nodes from AST
        condition = currentNode.condition
        body = currentNode.body
        beforeloop = currentNode.beforeLoop
        afterloop = currentNode.afterLoop
        if beforeloop:
            beforeloop.accept(self)

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
        self.llvm += "br i1 %" + str(reg[0]) + ", label %" + str(bodylabel) + " , label %" + "CONTINUE" + str(id(currentNode)) + "\n"

        # Body part
        self.llvm += "\n"
        self.llvm += str(bodylabel) + ":\n"
        body.accept(self)
        if "BREAK" in self.llvm:
            self.llvm = self.llvm[:(self.llvm.rfind("BREAK"))]


        # After loop
        if afterloop:
            # After label
            afterlabel = self.instr
            self.instr += 1
            self.llvm += "br label %" + str(afterlabel) + "\n"
            self.llvm += "\n"
            self.llvm += str(afterlabel) + ":\n"
            afterloop.accept(self)

            #self.llvm += "br label %" + "CONTINUE" + str(id(currentNode)) + "\n"

        # Label continue
        continuelabel = self.instr
        self.instr += 1
        self.llvm += "br label %" + str(conditionlabel) + "\n"
        # Continue part
        self.llvm += "\n"
        self.llvm += str(continuelabel) + ":\n"
        self.llvm = self.llvm.replace("CONTINUE" + str(id(currentNode)), str(continuelabel))
        self.llvm = self.llvm.replace("CONDITION" + str(id(currentNode)), str(conditionlabel))

        self.currentLoop.append(str(id(currentNode)))
        # After visiting scope, delete the symbol table
        self.currentTable.parent.children.remove(self.currentTable)
        self.currentTable = parent
        return currentNode

    def VisitVariable(self, currentNode):
        print("Variable")
        # For lvalue's look for the register
        if self.lvalue:
            print(currentNode.value)
            if self.currentTable.lookup(currentNode.value):
                return (str(self.currentTable.lookup(currentNode.value).register), str(self.currentTable.lookup(currentNode.value).type), "reg", currentNode.value)
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

            if "int*" in type:
                llvmrtyp = symbol.type.replace("int", "i32")
                self.llvm += "%" + str(self.instr) + " = load " + llvmrtyp + ", " + llvmrtyp + "* %" + str(
                    symbol.register) + ", align 8\n"
                self.instr += 1
                return (str(self.instr - 1), type[:-1], "reg", currentNode.value)
            if "float*" in type:
                llvmrtyp = symbol.type.replace("float", "float")
                self.llvm += "%" + str(self.instr) + " = load " + llvmrtyp + ", " + llvmrtyp + "* %" + str(
                    symbol.register) + ", align 8\n"
                self.instr += 1
                return (str(self.instr - 1), type[:-1], "reg", currentNode.value)
            if "char*" in type:
                llvmrtyp = symbol.type.replace("char", "i8")
                self.llvm += "%" + str(self.instr) + " = load " + llvmrtyp + ", " + llvmrtyp + "* %" + str(
                    symbol.register) + ", align 8\n"
                self.instr += 1
                return (str(self.instr - 1), type[:-1], "reg", currentNode.value)

            return (str(self.instr-1), type, "reg", currentNode.value)

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
                print("Variable")
            elif isinstance(child, Constant):
                print("Constant")
            children.append(child)

        left = currentNode.children[0].accept(self)
        right = currentNode.children[1].accept(self)
        print("The operands are:")
        print(left)
        print(right)
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
        else:
            BinType = "int"


        if BinType == "float":
            if lefttype == "int":
                self.llvm += "%" + str(self.instr) + " = sitofp i32 " + str(leftvalue) + " to float\n"
                leftvalue = "%" + str(self.instr)
                self.instr += 1
            elif righttype == "int":
                self.llvm += "%" + str(self.instr) + " = sitofp i32 " + str(rightvalue) + " to float\n"
                rightvalue = "%" + str(self.instr)
                self.instr += 1
        print("Binary operator:")
        print(currentNode.value)
        print("BinType")
        print(BinType)
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
                self.instr += 1
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
                    self.llvm += "%" + str(self.instr) + " = icmp sle i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
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
                    self.llvm += "%" + str(self.instr) + " = icmp sge i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
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
                self.lvalue = True
                node = currentNode.children[0].accept(self)
                return node
            case "*":
                #node = currentNode.children[0].accept(self)
                var = ""
                if self.lvalue:
                    if currentNode.children:
                        for child in currentNode.children:
                            if isinstance(child, Variable):
                                variable = self.currentTable.lookup(child.value)
                                var = (str(variable.register), str(variable.type), "reg", currentNode.value)

                                if "int*" in var[1]:
                                    llvmrtyp = var[1].replace("int", "i32")
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* %" + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                elif "float*" in var[1]:
                                    llvmrtyp = var[1].replace("float", "float")
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* %" + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                else:
                                    llvmrtyp = var[1].replace("char", "i8")
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* %" + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                # INT OOG HOUDE
                                var = (str(self.instr-1), str(variable.type), "reg", currentNode.value)
                            else:
                                return child.visit(self)
                else:
                    if currentNode.children:
                        for child in currentNode.children:
                            if isinstance(child, Variable):
                                variable = self.currentTable.lookup(child.value)
                                var = (str(variable.register), str(variable.type), "reg", child.value)
                                if "int*" in var[1]:
                                    llvmrtyp = var[1].replace("int", "i32")
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* %" + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                elif "float*" in var[1]:
                                    llvmrtyp = var[1].replace("float", "float")
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* %" + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                else:
                                    llvmrtyp = var[1].replace("char", "i8")
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* %" + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                var = (str(self.instr-1), str(variable.type[:-1]), "reg", var[3])
                            else:
                                var = child.accept(self)
                                llvmrtyp = var[1].replace("int", "i32")
                                if "int*" in var[1]:
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* %" + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                elif "float*" in var[1]:
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* %" + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                else:
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* %" + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                var = (str(self.instr-1), str(var[1][:-1]), "reg", var[3])
                if "*" not in var[1]:
                    if "int" in var[1]:
                        self.llvm += "%" + str(self.instr) + " = load i32, i32* %" + str(
                            self.instr - 1) + ", align 4\n"
                        self.instr += 1
                    elif "float" in var[1]:
                        self.llvm += "%" + str(self.instr) + " = load float, float* %" + str(
                            self.instr - 1) + ", align 4\n"
                        self.instr += 1
                    else:
                        self.llvm += "%" + str(self.instr) + " = load i8, i8* %" + str(
                            self.instr - 1) + ", align 1\n"
                        self.instr += 1
                    var = (str(self.instr - 1), str(var[1]), "reg", var[3])
                    return var
                else:
                    return var

            case "++":
                for child in currentNode.children:
                    if isinstance(child, Variable):
                        var = self.currentTable.lookup(child.value)
                        match var.type:
                            case "int":
                                self.llvm += "%" + str(self.instr) + " = load i32, i32* %" + str(var.register) + ", align 4\n"
                                self.instr += 1
                                self.llvm += "%" + str(self.instr) + " = add nsw i32 %" + str(self.instr-1) + ", 1\n"
                                self.instr += 1
                                self.llvm += "store i32 %" + str(self.instr-1) + ", i32* %" + str(var.register) + ", align 4\n"
                                return (str(self.instr-2) , str(var.type), "reg", str(child.value))
            case "--":
                for child in currentNode.children:
                    if isinstance(child, Variable):
                        var = self.currentTable.lookup(child.value)
                        match var.type:
                            case "int":
                                self.llvm += "%" + str(self.instr) + " = load i32, i32* %" + str(var.register) + ", align 4\n"
                                self.instr += 1
                                self.llvm += "%" + str(self.instr) + " = sub nsw i32 %" + str(self.instr-1) + ", 1\n"
                                self.instr += 1
                                self.llvm += "store i32 %" + str(self.instr-1) + ", i32* %" + str(var.register) + ", align 4\n"
                                return (str(self.instr-2) , str(var.type), "reg", str(child.value))
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
        try:
            value = int(currentNode.value)
        except ValueError:
            try:
                value = float(currentNode.value)
            except ValueError:
                value = currentNode.value
        if isinstance(value, int):
            return (value, "int", "value")
        elif isinstance(value, float):
            return (value, "float", "value")
        else:
            return (value, "char", "value")

    def VisitDeclaration(self, currentNode):
        #print("Declaration2LLVM")
        var = currentNode.var
        #print(var)
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
            self.lvalue = False
            value = currentNode.rvalue.accept(self)
            self.lvalue = True
            ltype = self.currentTable.lookup(currentNode.lvalue.var).type
            if value[2] != "reg":
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
                    packed = struct.pack("f", value)
                    unpacked = struct.unpack("f", packed)[0]
                    self.llvm += "store float " + str(unpacked) + ", float* %" + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "char":
                    value = value[0].replace("'", "")
                    if len(value) > 1:
                        value= value.encode('utf-8').decode('unicode-escape')
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
                        self.llvm += "%" + str(value[0]) + " = fptosi float %" + str(value[0]) + " to i32\n"
                        self.instr += 1
                    self.llvm += "store i32 %" + str(value[0]) + ", i32* %" + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "float":
                    if value[1] == "int":
                        self.llvm += "%" + str(value[0]) + " = sitofp i32 %" + str(value[0]) + " to float\n"
                        self.instr += 1
                    self.llvm += "store float %" + str(value[0]) + ", float* %" + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                elif ltype == "char":
                    self.llvm += "store i8 %" + str(value[0]) + ", i8* %" + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 1\n"
                elif "int*" == ltype:
                    self.llvm += "store i32* %" + str(value[0]) + ", i32** %" + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 8\n"
                elif  "float*" == ltype:
                    self.llvm += "store float* %" + str(value[0]) + ", float** %" + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 8\n"
                elif "char*" == ltype:
                    self.llvm += "store i8* %" + str(value[0]) + ", i8** %" + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 1\n"
                elif "int*" in ltype:
                    # We need to dereference more
                    if ltype != value[1]:
                        llvmltyp = ltype.replace("int", "i32")
                        llvmrtyp = value[1].replace("int", "i32")
                        self.llvm += "store "+ str(llvmrtyp) + "* %" + str(value[0]) + ", " + str(llvmltyp) + "* %" + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 8\n"
                    else:
                        llvmltyp = ltype.replace("int", "i32")
                        llvmrtyp = value[1].replace("int", "i32")
                        self.llvm += "store " + str(llvmrtyp) + "* %" + str(value[0]) + ", " + str(
                            llvmltyp) + "* %" + str(
                            self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 8\n"

                elif "int*" in ltype:
                    # We need to dereference more
                    self.llvm += "store float* %" + str(value[0]) + ", float** %" + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 8\n"
                elif "int*" in ltype:
                    # We need to dereference more
                    self.llvm += "store i8* %" + str(value[0]) + ", i8** %" + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 1\n"
                else:
                    print("test")

        # The lvalue is no declaration but a variable
        elif isinstance(currentNode.lvalue, Variable):
            self.lvalue = False
            value = currentNode.rvalue.accept(self)
            self.lvalue = True
            reg = currentNode.lvalue.accept(self)
            #ltype = self.symbolTable.lookup(currentNode.lvalue.children[0].value).type
            ltype = self.currentTable.lookup(currentNode.lvalue.value).type
            #self.instr += 1
            if ltype == "int*":
                self.llvm += "store i32* %" + str(value[0]) + ", i32** %" + str(reg[0]) + ", align 8\n"
            if ltype == "float*":
                self.llvm += "store float* %" + str(value[0]) + ", float** %" + str(reg[0]) + ", align 8\n"
            if ltype == "char*":
                self.llvm += "store i8* %" + str(value[0]) + ", i8** %" + str(reg[0]) + ", align 1\n"
            if value[2] != "reg":
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
                    packed = struct.pack("f", value)
                    unpacked = struct.unpack("f", packed)[0]
                    self.llvm += "store float " + str(unpacked) + ", float* %" + self.currentTable.lookup(currentNode.lvalue.value).register + ", align 4\n"
                elif ltype == "char":
                    value = value[0].replace("'","")
                    if len(value) > 1:
                        value= value.encode('utf-8').decode('unicode-escape')
                    self.llvm += "store i8 " + str(ord(value)) + ", i8* %" + self.currentTable.lookup(currentNode.lvalue.value).register + ", align 1\n"
            else:
                if ltype == "int":
                    self.llvm += "store i32 %" + str(value[0]) + ", i32* %" + reg[0] + ", align 4\n"
                elif ltype == "float":
                    #packed = struct.pack("f", value[0])
                    #unpacked = struct.unpack("f", packed)[0]
                    self.llvm += "store float %" + str(value[0]) + ", float* %" + reg[0] + ", align 4\n"
                elif ltype == "char":
                    value = value.replace("'","")
                    self.llvm += "store i8 " + str(ord(value[0])) + ", i8* %" + reg[0] + ", align 1\n"
        else:
            # In this case the lvalue is a pointer dereference
            value = currentNode.rvalue.accept(self)
            self.lvalue = True
            reg = currentNode.lvalue.accept(self)
            var = reg[3]
            type = reg[1]
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
                    packed = struct.pack("f", value[0])
                    unpacked = struct.unpack("f", packed)[0]
                    self.llvm += "store float " + str(unpacked) + ", float* %" + str(self.instr-1) + ", align 4\n"
            if type == "char*":
                value = value[0].replace("'", "")
                self.llvm += "store i8 " + str(ord(value[0])) + ", i8* %" + str(self.instr-1) + ", align 1\n"
        return currentNode

    def VisitMLComment(self, currentNode):
        #print("MLComment")
        comment = currentNode.value
        comment = ";" + comment
        comment = comment.replace("\n" , "\n;")
        self.llvm += comment + "\n"
        return currentNode

    def VisitSLComment(self, currentNode):
        #print("SLComment")
        comment = currentNode.value
        comment = comment.replace("//", ";")
        self.llvm += comment + "\n"
        return currentNode

    def VisitScanf(self, currentNode):
        print("Scanf")
        format = currentNode.format.value
        print(format)
        params = []
        if not self.scanning:
            self.llvm = "declare i32 @__isoc99_scanf(i8* noundef, ...)\n" + self.llvm

        # Prepare arguments
        if currentNode.args:
            for child in currentNode.args.children:
                print(child)
                self.lvalue = False
                node = child.accept(self)
                self.lvalue = True
                print(node)
                # When the arg is reference and no value
                if isinstance(child, UnaryOperation):
                    node = (node[0], node[1], node[2], node[3], "ref")
                    params.append(node)
                # When the arg is a value
                elif node[2] == "reg":
                    symbol = self.currentTable.lookup(node[3])
                    type = symbol.type
                    print(type)
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
                    '''
                    if type == "int*":
                        self.llvm += "%" + str(self.instr) + " = load i32, i32* %" + str(
                            node[0]) + ", align 1\n"
                        self.instr += 1
                    if type == "float*":
                        self.llvm += "%" + str(self.instr) + " = load float, float* %" + str(
                            node[0]) + ", align 1\n"
                        self.instr += 1
                    if type == "char*":
                        self.llvm += "%" + str(self.instr) + " = load i8, i8* %" + str(
                            node[0]) + ", align 1\n"
                        self.instr += 1
                    '''
                    newnode = (self.instr - 1, node[1], node[2], node[3], "value")
                    params.append(newnode)
                else:
                    print(node)
                    params.append(node)

        if format in self.printstr:
            print("string exists")
        else:
            size = len(format)-1
            print("The format has size:")
            print(size)
            strindex = len(self.printstr)
            '''
            packed = struct.pack("18c", format)
            print(packed)
            unpacked = struct.unpack("c", packed)[0]
            print(unpacked)
            '''
            self.llvm = "@.str." + str(strindex) + " = private unnamed_addr constant [" + str(size) + " x i8] c" + format[:-1] + "\\00" + "\", align 1\n" + self.llvm
            self.printstr.append(format)

        # Print function call
        self.llvm += "%" + str(self.instr) + " = call i32 (i8*, ...)" + " @__isoc99_scanf(i8* noundef getelementptr inbounds "
        self.llvm += "([" + str(size) + " x i8], ["+ str(size) + " x i8]* @.str." + str(strindex) + ", i64 0, i64 0)"
        print("Parameters:")
        i = 1
        numberParams = len(params)
        print(numberParams)
        if params:
            self.llvm += ", "
        for node in params:
            print(node)
            if node[2] == "reg" and node[4] == "value":
                if node[1] == "int":
                    self.llvm += "i32* noundef %" + str(node[0])
                elif node[1] == "float":
                    self.llvm += "float* noundef %" + str(node[0])
                else:
                    self.llvm += "i8 noundef %" + str(node[0])
            elif node[2] == "reg" and node[4] == "ref":
                if "int" in node[1]:
                    self.llvm += "i32* noundef %" + str(node[0])
                elif "float" in node[1]:
                    self.llvm += "float* noundef %" + str(node[0])
                else:
                    self.llvm += "i8* noundef %" + str(node[0])
            elif node[2] == "value":
                if node[1] == "int":
                    self.llvm += "i32 noundef " + str(node[0])
                elif node[1] == "float":
                    self.llvm += "float noundef " + str(node[0])
                else:
                    self.llvm += "i8 noundef " + str(node[0])

            if i != numberParams:
                self.llvm += ", "
            i += 1
        self.llvm += ")"
        self.llvm += "\n"
        self.instr += 1
        return currentNode

    def VisitPrintf(self, currentNode):
        print("Printf")
        format = currentNode.format.value
        print(format)
        params = []
        if not self.printing:
            self.llvm = "declare i32 @printf(i8* noundef, ...)\n" + self.llvm

        # Prepare arguments
        if currentNode.args:
            for child in currentNode.args.children:
                print(child)
                self.lvalue = False
                node = child.accept(self)
                self.lvalue = True
                print(node)
                # When the arg is reference and no value
                if isinstance(child, UnaryOperation):
                    node = (node[0], node[1], node[2], node[3], "ref")
                    params.append(node)
                # When the arg is a value
                elif node[2] == "reg":
                    symbol = self.currentTable.lookup(node[3])
                    type = symbol.type
                    '''
                    if type == "int":
                        self.llvm += "%" + str(self.instr) + " = load i32, i32* %" + str(
                            node[0]) + ", align 4\n"
                        self.instr += 1
                    if type == "float":
                        self.llvm += "%" + str(self.instr) + " = load float, float* %" + str(
                            node[2]) + ", align 4\n"
                        self.instr += 1
                    if type == "char":
                        self.llvm += "%" + str(self.instr) + " = load i8, i8* %" + str(
                            node[2]) + ", align 1\n"
                        self.instr += 1
                    '''
                    newnode = (self.instr - 1, node[1], node[2], node[3], "value")
                    params.append(newnode)
                else:
                    print(node)
                    params.append(node)

        if format in self.printstr:
            print("string exists")
        else:
            size = len(format)-1
            print("The format has size:")
            print(size)
            strindex = len(self.printstr)
            '''
            packed = struct.pack("18c", format)
            print(packed)
            unpacked = struct.unpack("c", packed)[0]
            print(unpacked)
            '''
            self.llvm = "@.str." + str(strindex) + " = private unnamed_addr constant [" + str(size) + " x i8] c" + format[:-1] + "\\00" + "\", align 1\n" + self.llvm
            self.printstr.append(format)

        # Print function call
        self.llvm += "%" + str(self.instr) + " = call i32 (i8*, ...)" + " @printf(i8* noundef getelementptr inbounds "
        self.llvm += "([" + str(size) + " x i8], ["+ str(size) + " x i8]* @.str." + str(strindex) + ", i64 0, i64 0)"
        print("Parameters:")
        i = 1
        numberParams = len(params)
        print(numberParams)
        if params:
            self.llvm += ", "
        for node in params:
            print(node)
            if node[2] == "reg" and node[4] == "value":
                if node[1] == "int":
                    self.llvm += "i32 noundef %" + str(node[0])
                elif node[1] == "float":
                    self.llvm += "float noundef %" + str(node[0])
                else:
                    self.llvm += "i8 noundef %" + str(node[0])
            elif node[2] == "reg" and node[4] == "ref":
                if "int" in node[1]:
                    self.llvm += "i32 noundef %" + str(node[0])
                elif "float" in node[1]:
                    self.llvm += "float noundef %" + str(node[0])
                else:
                    self.llvm += "i8 noundef %" + str(node[0])
            elif node[2] == "value":
                if node[1] == "int":
                    self.llvm += "i32 noundef " + str(node[0])
                elif node[1] == "float":
                    self.llvm += "float noundef " + str(node[0])
                else:
                    self.llvm += "i8 noundef " + str(node[0])

            if i != numberParams:
                self.llvm += ", "
            i += 1
        self.llvm += ")"
        self.llvm += "\n"
        self.instr += 1













        '''
        self.lvalue = False
        node = currentNode.children[0].accept(self)
        self.lvalue = True
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
            if not self.printing:
                self.llvm = "declare i32 @printf(i8* noundef, ...)\n" + self.llvm
            if isinstance(node, ASTNode):
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
                    if len(value) > 1:
                        value= value.encode('utf-8').decode('unicode-escape')
                    self.llvm += "store i8 " + str(ord(value)) + ", i8* %" + str(self.instr - 1) + ", align 4\n"
                    self.llvm += "%" + str(self.instr) + " = load i8, i8* %" + str(self.instr - 1) + ", align 4\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = sext i8 %" + str(int(self.instr) - 1) + " to i32\n"
                    self.instr += 1
                    self.llvm += "%" + str(
                        self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                      "@.char, i64 0, i64 0), i32 noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
            else:
                if node[1] == "int":
                    if not self.intprinting:
                        self.llvm = "@.int = private unnamed_addr constant [3 x i8] c" + "\"" + "%d" + "\\00" + "\", align 1\n" \
                                    + self.llvm
                        self.intprinting = True
                        self.printing = True

                    self.llvm += "%" + str(
                        self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                      "@.int, i64 0, i64 0), i32 noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
                if node[1] == "float":
                    if not self.floatprinting:
                        self.llvm = "@.float = private unnamed_addr constant [3 x i8] c" + "\"" + "%f" + "\\00" + "\", align 1\n" \
                                    + self.llvm
                        self.floatprinting = True
                        self.printing = True

                    self.llvm += "%" + str(self.instr) + " = fpext float %" + str(int(self.instr) - 1) + " to double\n"
                    self.instr += 1
                    self.llvm += "%" + str(
                        self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                      "@.float, i64 0, i64 0), double noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
                if node[1] == "char":
                    if not self.charprinting:
                        self.llvm = "@.char = private unnamed_addr constant [3 x i8] c" + "\"" + "%c" + "\\00" + "\", align 1\n"\
                                     + self.llvm
                        self.charprinting = True
                        self.printing = True

                    self.llvm += "%" + str(self.instr) + " = sext i8 %" + str(int(self.instr) - 1) + " to i32\n"
                    self.instr += 1
                    self.llvm += "%" + str(self.instr) + " = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([3 x i8], [3 x i8]* " \
                                 "@.char, i64 0, i64 0), i32 noundef %" + str(int(self.instr) - 1) + ")\n"
                    self.instr += 1
            '''
        return currentNode


