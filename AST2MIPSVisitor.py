import SymbolTable
from AST import *
import graphviz
from SymbolTable import *
from Context import *
import re
import struct
from FunctionContext import *

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class AST2MIPSVisitor(Visitor):

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
    globalPosition = 0
    FCStack = 0

    def __init__(self, llvm="", symbolTable=SymbolTable()):
        #print("----------------Converting AST 2 LLVM IR----------------")

        # The generated LLVM IR code
        self.llvm = llvm

        #self.symbolTable = symbolTable

        # Set the current symbol table which will be used
        self.currentTable = symbolTable

        self.currentLoop = []

        self.printstr.clear()
        self.FCStack = FCStack()

    def allocateRegister(self, table, name, var):
        type = var.type
        attr = var.attr
        size = 0
        if isinstance(var, Array):
            size = var.size
        if type == "int":
            #self.llvm += "%" + str(self.instr) + " = alloca i32, align 4\n"
            table.insertRegister(name, str(self.FCStack.getCurrentOffset()))
            #self.instr += 1
        elif type == "float":
            #self.llvm += "%" + str(self.instr) + " = alloca float, align 4\n"
            table.insertRegister(name, str(self.FCStack.getCurrentOffset()))
            self.instr += 1
        elif type == "char":
            #self.llvm += "%" + str(self.instr) + " = alloca i8, align 1\n"
            table.insertRegister(name, str(self.FCStack.getCurrentOffset()))
            #self.instr += 1
        elif "int*" in type:
            '''
            #llvmtyp = type.replace("int","i32")
            #self.llvm += "%" + str(self.instr) + " = alloca " + str(llvmtyp) + ", align 8\n"
            #table.insertRegister(name, "%"+str(self.instr))
            #self.instr += 1
            '''
            table.insertRegister(name, str(self.FCStack.getCurrentOffset()))
        elif "float*" in type:
            '''
            #llvmtyp = type.replace("float", "float")
            #self.llvm += "%" + str(self.instr) + " = alloca " + str(llvmtyp) + ", align 8\n"
            #table.insertRegister(name, "%"+str(self.instr))
            #self.instr += 1
            '''
            table.insertRegister(name, str(self.FCStack.getCurrentOffset()))
        elif "char*" in type:
            '''
            #llvmtyp = type.replace("char", "i8")
            #self.llvm += "%" + str(self.instr) + " = alloca " + str(llvmtyp) + ", align 8\n"
            #table.insertRegister(name, "%"+str(self.instr))
            #self.instr += 1
            '''
            table.insertRegister(name, str(self.FCStack.getCurrentOffset()))
        elif "[]" in type:
            size = self.currentTable.lookupUnallocated(name).size
            if "int" in type:
                arraytype = type.replace("int","i32")
                arraytype = arraytype.replace("[]", "")
                self.llvm += "%" + str(self.instr) + " = alloca [" + str(size) + " x " + str(arraytype) + "], align 16\n"
                table.insertRegister(name, "%"+str(self.instr))
                self.instr += 1
            if "float" in type:
                arraytype = type.replace("float","float")
                arraytype = arraytype.replace("[]", "")
                self.llvm += "%" + str(self.instr) + " = alloca [" + str(size) + " x " + str(arraytype) + "], align 16\n"
                table.insertRegister(name, "%"+str(self.instr))
                self.instr += 1
            if "char" in type:
                arraytype = type.replace("char","i8")
                arraytype = arraytype.replace("[]", "")
                self.llvm += "%" + str(self.instr) + " = alloca [" + str(size) + " x " + str(arraytype) + "], align 16\n"
                table.insertRegister(name, "%"+str(self.instr))
                self.instr += 1
        else:
            print("Type not implemented")

    def allocateRegisters(self, table):
        #print("Allocating registers:")
        for key, value in table.vars.items():
            self.allocateRegister(table, key, value)

        for child in table.children:
            self.allocateRegisters(child)

    def allocateRegistersCurrentScope(self, table):
        #print("Allocating registers:")
        i = 0
        for key, value in table.vars.items():
            self.allocateRegister(table, key, value)
            i += 1
        return i

    def VisitASTNode(self, currentNode):
        #print("Node")
        if self.currentTable.lookup(currentNode.value):
            return (str(self.currentTable.lookup(currentNode.value).register), str(self.currentTable.lookup(currentNode.value).type), "reg")
        else:
            if len(currentNode.children) == 1:
                return currentNode.children[0].accept(self)
            for child in currentNode.children:
                node = child.accept(self)
            return currentNode

    def VisitInclude(self, currentNode):
        return currentNode
    def VisitExprLoop(self, currentNode):
        #print("ExprLoop")
        for child in currentNode.children:
            node = child.accept(self)
        return currentNode

    def VisitCall(self, currentNode):
        #print("VisitCall")
        #print("Look for :")
        #print(currentNode.value)
        params = []
        #print(currentNode.children)

        # Prepare arguments
        for child in currentNode.children:
            #print(child)
            self.lvalue = False
            node = child.accept(self)
            #print("Prepared:")
            #print(node)
            # When the arg is reference and no value
            if isinstance(child, UnaryOperation):
                node = (node[0], node[1], node[2], node[3], "ref")
                params.append(node)
                #print("test")
            # When the arg is a value
            elif node[2] == "reg":
                #print(len(node))
                if len(node) > 4:
                    if node[4] != "value":
                        symbol = self.currentTable.lookup(node[3])
                        type = symbol.type
                        if type == "int":
                            self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(
                                symbol.register) + ", align 4\n"
                            self.instr += 1
                        if type == "float":
                            self.llvm += "%" + str(self.instr) + " = load float, float* " + str(
                                symbol.register) + ", align 4\n"
                            self.instr += 1
                        if type == "char":
                            self.llvm += "%" + str(self.instr) + " = load i8, i8* " + str(
                                symbol.register) + ", align 1\n"
                            self.instr += 1
                    newnode = ("%" + str(self.instr - 1), node[1], node[2], node[3], "value")
                elif len(node) > 3:
                    symbol = self.currentTable.lookup(node[3])
                    type = symbol.type
                    if "*" not in type:
                        if type == "int":
                            self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(
                                symbol.register) + ", align 4\n"
                            self.instr += 1
                        if type == "float":
                            self.llvm += "%" + str(self.instr) + " = load float, float* " + str(
                                symbol.register) + ", align 4\n"
                            self.instr += 1
                        if type == "char":
                            self.llvm += "%" + str(self.instr) + " = load i8, i8* " + str(
                                symbol.register) + ", align 1\n"
                            self.instr += 1
                        newnode = ("%"+str(self.instr - 1), node[1], node[2], node[3], "value")
                    else:
                        newnode = (node[0], node[1], node[2], node[3], "ref")
                else:
                    type = node[1]
                    if type == "int":
                        self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(
                            node[0]) + ", align 4\n"
                        self.instr += 1
                    if type == "float":
                        self.llvm += "%" + str(self.instr) + " = load float, float* " + str(
                            node[0]) + ", align 4\n"
                        self.instr += 1
                    if type == "char":
                        self.llvm += "%" + str(self.instr) + " = load i8, i8* " + str(
                            node[0]) + ", align 1\n"
                        self.instr += 1
                    newnode = ("%" + str(self.instr - 1), node[1], node[2], "", "value")
                params.append(newnode)
            else:
                #print(node)
                params.append(node)
        #print("#params")
        #print(len(params))

        # Print function call
        func = self.currentTable.lookup(currentNode.value.replace("()",""))
        #print(func)
        #print(func.attr)
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
            #print("Parameters:")
            i = 1
            numberParams = len(currentNode.children)
            for node in params:
                #print(node)
                if node[2] == "reg" and node[4] == "value":
                    if node[1] == "int":
                        self.llvm += "i32 noundef " + str(node[0])
                    elif node[1] == "float":
                        self.llvm += "float noundef " + str(node[0])
                    elif node[1] == "char":
                        self.llvm += "i8 noundef " + str(node[0])
                elif node[2] == "reg" and node[4] == "ref":
                    if "int" in node[1]:
                        self.llvm += "i32* noundef " + str(node[0])
                    elif "float" in node[1]:
                        self.llvm += "float* noundef " + str(node[0])
                    elif "char" in node[1]:
                        self.llvm += "i8* noundef " + str(node[0])
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
        return ("%" + str(self.instr-1), func.type, "reg", str(currentNode.value), "value")

    def VisitFunction(self, currentNode):
        #print("Function")
        self.instr = 0
        hasreturn = len(self.context)
        if currentNode.hasbody:
            # Open a new scope by selecting the right symbol table
            parent = self.currentTable
            self.currentTable = self.currentTable.children[0]

            context = Context()
            self.context.append(context)

            returntype = currentNode.returnType.value
            context.returnType = returntype

            funcname = currentNode.value
            self.llvm += funcname + ": \n"

            # Save registers in Callee
            fcontext = FunctionContext()
            self.FCStack.push(fcontext)
            print("number of vars")
            size = self.currentTable.getNumberOfVariables()
            print(str(size))
            print("__")
            numberOfParams = len(self.currentTable.vars)
            fcontext.offset = (size + 2)*4
            self.llvm += "addiu $sp, $sp, -" + str(fcontext.offset) + "\n"
            fcontext.offset -= 4
            self.llvm += "sw $ra, " + str(fcontext.offset) + "($sp)" + "\n"
            fcontext.offset -= 4
            self.llvm += "sw $fp, " + str(fcontext.offset) + "($sp)" + "\n"
            fcontext.offset -= 4
            i = 0
            '''
            for var in self.currentTable.vars:
                self.llvm += "sw $s" + str(i) + ", " + str(fcontext.offset) + "($sp)" + "\n"
                fcontext.offset -= 4
            '''
            self.llvm += "move $fp, $sp \n"
            roffset = fcontext.offset+4
            fcontext.roffset = roffset
            '''
            if currentNode.params:
                params = currentNode.params
                for param in params:
                    param2 = self.currentTable.lookupInThisTable(param.var)
                    node = param.accept(self)
                    paramtype = param2.type
                    reg = self.currentTable.lookupInThisTable(node.var).register
            '''

            if currentNode.body:
                node = currentNode.body.accept(self)
            newhasreturn = len(self.context)
            #print("New #return in stack")
            #print(context.hasReturn)
            if not context.hasReturn and context.returnRegister == -1:
                self.llvm += "ret void\n"
            elif not context.hasReturn:
                if "int" in context.returnType:
                    ret = context.returnType.replace("int", "i32")
                    self.llvm += "ret " + ret + " " + str(context.returnRegister) + "\n"
                elif "float" in context.returnType:
                    ret = context.returnType.replace("float", "float")
                    self.llvm += "ret " + ret + " " + str(context.returnRegister) + "\n"
                elif "char" in context.returnType:
                    ret = context.returnType.replace("char", "i8")
                    self.llvm += "ret " + ret + " " + str(context.returnRegister) + "\n"

            # Restore register in Callee
            offset = self.FCStack.getRestoreOffset()
            self.llvm += "move $fp, $sp \n"
            i = 0
            '''
            for var in self.currentTable.vars:
                self.llvm += "sw $s" + str(i) + ", " + str(offset) + "($sp)" + "\n"
                offset += 4
            '''
            self.llvm += "sw $fp, " + str(offset) + "($sp)" + "\n"
            offset += 4
            self.llvm += "sw $ra, " + str(offset) + "($sp)" + "\n"
            offset += 4

            self.llvm += "addiu $sp, $sp, " + str(offset) + "\n"
            self.FCStack.pop()
            if(funcname == "main"):
                self.llvm += "li $v0, 10 \n"
                self.llvm += "syscall \n"
            self.context.pop()
            # After visiting scope, delete the symbol table
            self.currentTable.parent.children.remove(self.currentTable)
            self.currentTable = parent
            #self.llvm += "}\n"
        return currentNode

    def VisitJump(self, currentNode):
        #print("Jump")
        if currentNode.value == "break":
            currentid = self.currentLoop.pop()
            #print(currentid)
            self.llvm += "br label %" + "CONTINUE" + currentid[0] + "            ;break\n"
            self.llvm += "BREAK"
            self.currentLoop.append((currentid[0], "break"))
        elif currentNode.value == "continue":
            currentid = self.currentLoop.pop()
            #print(currentid)
            self.llvm += "br label %" + "CONDITION" + currentid[0] + "            ;continue\n"
            self.llvm += "NEXTLOOP"
            self.currentLoop.append((currentid[0], "continue"))
        elif currentNode.value == "return":
            if currentNode.children:
                self.lvalue = False
                result = currentNode.children[0].accept(self)
                self.lvalue = True
                #print(result)
            else:
                result = ("0", "", "value")
            #print(currentNode.type)
            if currentNode.type == "int":
                if result[2] == "reg":
                    reg = self.loadRegister(result[0])
                    self.llvm += "ret i32 " + str(reg) + "\n"
                else:
                    self.llvm += "ret i32 " + str(result[0]) + "\n"
            if currentNode.type == "float":
                if result[2] == "reg":
                    reg = self.loadRegister(result[0])
                    self.llvm += "ret float " + str(reg) + "\n"
                else:
                    self.llvm += "ret float " + str(result[0]) + "\n"
            if currentNode.type == "char":
                if result[2] == "reg":
                    reg = self.loadRegister(result[0])
                    self.llvm += "ret i8 " + str(reg) + "\n"
                else:
                    self.llvm += "ret i8 " + str(result[0]) + "\n"
            if currentNode.type == "void":
                self.llvm += "ret void\n"
            self.instr += 1
            context = self.context.pop()
            context.hasReturn = True
            self.context.append(context)
        return currentNode

    def loadRegister(self, register):
        symbol = self.currentTable.lookupByRegister(register)
        if symbol:
            type = symbol.type
            if type == "int":
                self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(
                    symbol.register) + ", align 4\n"
                self.instr += 1
            if type == "float":
                self.llvm += "%" + str(self.instr) + " = load float, float* " + str(
                    symbol.register) + ", align 4\n"
                self.instr += 1
            if type == "char":
                self.llvm += "%" + str(self.instr) + " = load i8, i8* " + str(
                    symbol.register) + ", align 1\n"
                self.instr += 1
            return "%" + str(self.instr - 1)
        return "%" + str(self.instr - 1)

    def VisitConditional(self, currentNode):
        #print("Conditional")
        # Get the usefull nodes from AST
        cond = currentNode.condition
        ifbody = currentNode.ifbody
        elsebody = currentNode.elsebody

        #Add context
        context = Context()
        self.context.append(context)

        # Visit condition to get code
        reg = cond.accept(self)
        print(reg)
        '''
        if reg[1] == "float":
            self.llvm += "%" + str(self.instr) + " = fcmp une float " + reg[0] + ", 0.0\n"
            self.instr += 1
            reg = ("%"+ str(self.instr-1), reg[1], reg[2])
        elif reg[1] == "int":
            self.llvm += "%" + str(self.instr) + " = icmp ne i32 " + reg[0] + ", 0\n"
            self.instr += 1
            reg = ("%"+ str(self.instr-1), reg[1], reg[2])
        '''

        # Assign a label to the if body
        #iflabel = self.instr
        #self.instr += 1

        # If else body then add the label to the break instruction
        self.llvm += "addiu $at, $zero, 1\n"
        self.llvm += "beq $at, " + str(reg[0]) + ", IF" + str(id(context)) + "\n"

        if elsebody:
            #self.llvm += "br i1 " + str(reg[0]) + ", label %" + str(iflabel) + ", label %" + "ELSE" + str(id(currentNode)) + "\n"
            self.llvm += "j ELSE" + str(id(context)) + "\n"
        else:
            self.llvm += "j CONT" + str(id(context)) + "\n"

        # Add the label of the if body and visit the ifbody
        self.llvm += "\n"
        self.llvm += "IF" + str(id(context)) + ":\n"

        # Open a new scope by selecting the right symbol table
        parent = self.currentTable
        self.currentTable = self.currentTable.children[0]
        #self.allocateRegistersCurrentScope(self.currentTable)
        #print(self.currentTable)
        ifbody.accept(self)
        # After visiting scope, delete the symbol table
        self.currentTable.parent.children.remove(self.currentTable)
        self.currentTable = parent

        if "BREAK" in self.llvm:
            self.llvm = self.llvm[:(self.llvm.rfind("BREAK"))]
        elif "NEXTLOOP" in self.llvm:
            self.llvm = self.llvm[:(self.llvm.rfind("NEXTLOOP"))]
        else:
            #self.llvm += "br label %" + "CONTINUE" + str(id(currentNode))  + "\n"
            #self.llvm += "br label %" + "CONTINUE" + str(id(currentNode)) + "\n"
            self.llvm += "j CONT" + str(id(context)) + "\n"

        # If else body then add the label and visit the else body
        if elsebody:
            # If it has else, label else body
            #elselabel = self.instr
            #self.instr += 1
            #self.llvm = self.llvm.replace("ELSE" + str(id(currentNode)), str(elselabel))
            self.llvm += "\n"
            self.llvm += "ELSE" + str(id(context)) + ":\n"

            # Open a new scope by selecting the right symbol table
            parent = self.currentTable
            self.currentTable = self.currentTable.children[0]
            self.allocateRegistersCurrentScope(self.currentTable)
            elsebody.accept(self)
            # After visiting scope, delete the symbol table
            self.currentTable.parent.children.remove(self.currentTable)
            self.currentTable = parent

            if "BREAK" in self.llvm:
                self.llvm = self.llvm[:(self.llvm.rfind("BREAK"))]
            elif "NEXTLOOP" in self.llvm:
                self.llvm = self.llvm[:(self.llvm.rfind("NEXTLOOP"))]
            else:
                #self.llvm += "br label %" + "CONTINUE" + str(id(currentNode)) + "\n"
                self.llvm += "j CONT" + str(id(context)) + "\n"

        self.context.pop()

        # Add label to next instructions
        # Label the next instruction, so we can jump when ending if or else
        #continuelabel = self.instr
        #self.instr += 1
        #self.llvm = self.llvm.replace("CONTINUE" + str(id(currentNode)), str(continuelabel))
        self.llvm += "\n"
        self.llvm += "CONT" + str(id(context)) + ":\n"
        return currentNode

    def VisitScope(self, currentNode):
        #print("Scope")
        #print("Opening scope " + currentNode.value )

        # Open Context
        context = Context()
        self.context.append(context)

        # Open a new scope by selecting the right symbol table
        parent = self.currentTable
        self.currentTable = self.currentTable.children[0]
        #self.allocateRegistersCurrentScope(self.currentTable)

        # Visit scope body
        for child in currentNode.children:
            node = child.accept(self)

        # Close Context
        self.context.pop()

        # After visiting scope, delete the symbol table
        self.currentTable.parent.children.remove(self.currentTable)
        self.currentTable = parent
        return currentNode

    def VisitWhile(self, currentNode):
        #print("While")
        self.currentLoop.append((str(id(currentNode)), ""))

        # Open context
        context = Context()
        self.context.append(context)

        # Open a new scope by selecting the right symbol table
        parent = self.currentTable
        self.currentTable = self.currentTable.children[0]

        #self.allocateRegistersCurrentScope(self.currentTable)
        # Get corresponding nodes from AST
        condition = currentNode.condition
        body = currentNode.body
        beforeloop = currentNode.beforeLoop
        afterloop = currentNode.afterLoop
        if beforeloop:
            beforeloop.accept(self)

        # Label condition
        conditionlabel = self.instr
        self.instr += 1

        self.llvm += "j COND" + str(id(context)) + "\n"

        # Condition part
        self.llvm += "\n"
        self.llvm += "COND" + str(id(context)) + ":\n"
        reg = condition.accept(self)
        # Label body
        bodylabel = self.instr
        self.instr += 1
        #self.llvm += "br i1 " + str(reg[0]) + ", label %" + str(bodylabel) + " , label %" + "CONTINUE" + str(id(currentNode)) + "\n"
        self.llvm += "addiu $at, $zero, 1\n"
        self.llvm += "beq $at, " + str(reg[0]) + ", BODY" + str(id(context)) + "\n"
        self.llvm += "j CONT" + str(id(context)) + "\n"

        # Body part
        self.llvm += "\n"
        self.llvm += "BODY" + str(id(context)) + ":\n"
        body.accept(self)
        if "BREAK" in self.llvm:
            self.llvm = self.llvm[:(self.llvm.rfind("BREAK"))]


        # After loop
        if afterloop:
            # After label
            afterlabel = self.instr
            self.instr += 1
            #self.llvm += "br label %" + str(afterlabel) + "\n"
            self.llvm += "j CONT" + str(id(context)) + "\n"
            self.llvm += "\n"
            self.llvm += "CONT" + str(id(context)) + ":\n"
            afterloop.accept(self)

            #self.llvm += "br label %" + "CONTINUE" + str(id(currentNode)) + "\n"

        # Label continue
        continuelabel = self.instr
        self.instr += 1
        #self.llvm += "br label %" + str(conditionlabel) + "\n"
        self.llvm += "j COND" + str(id(context)) + "\n"
        # Continue part
        self.llvm += "\n"
        self.llvm += "CONT" + str(id(context)) + ":\n"
        self.llvm = self.llvm.replace("CONTINUE" + str(id(currentNode)), str(continuelabel))
        self.llvm = self.llvm.replace("CONDITION" + str(id(currentNode)), str(conditionlabel))


        self.currentLoop.append(str(id(currentNode)))

        # Close context
        self.context.pop()

        # After visiting scope, delete the symbol table
        self.currentTable.parent.children.remove(self.currentTable)
        self.currentTable = parent
        return currentNode

    def VisitVariable(self, currentNode):
        #print("Variable")
        # For lvalue's look for the register
        if self.lvalue:
            print("This lvalue?")
            #print(currentNode.value)
            #print(self.currentTable)
            if self.currentTable.lookup(currentNode.value):
                return (str(self.currentTable.lookup(currentNode.value).register), str(self.currentTable.lookup(currentNode.value).type), "reg", currentNode.value)
            else:
                return currentNode
        else:
            symbol = self.currentTable.lookup(currentNode.value)
            type = symbol.type
            if type == "int":
                reg = self.FCStack.getFreeTempReg()
                print("reg: " + str(reg))
                print("address:" + symbol.register)
                self.llvm += "lw $t" + str(reg) + " , " + symbol.register + "($fp)\n"
                reg = "$t" + str(reg)
                #self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(
                    #symbol.register) + ", align 4\n"
                #self.instr += 1
                self.FCStack.addTempReg(str(reg))
            if type == "float":
                reg = self.FCStack.getFreeFTempReg()
                self.llvm += "lwc1 $f" + str(reg) + " , " + symbol.register + "($fp)\n"
                reg = "$f" + str(reg)
                self.FCStack.addTempReg(str(reg))
                #self.llvm += "%" + str(self.instr) + " = load float, float* " + str(
                    #symbol.register) + ", align 4\n"
                #self.instr += 1
            if type == "char":
                reg = self.FCStack.getFreeTempReg()
                print("reg: " + str(reg))
                print("address:" + symbol.register)
                self.llvm += "lw $t" + str(reg) + " , " + symbol.register + "($fp)\n"
                reg = "$t" + str(reg)
                #self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(
                    #symbol.register) + ", align 4\n"
                #self.instr += 1
                self.FCStack.addTempReg(str(reg))

            if "int*" in type:
                llvmrtyp = symbol.type.replace("int", "i32")
                self.llvm += "%" + str(self.instr) + " = load " + llvmrtyp + ", " + llvmrtyp + "* " + str(
                    symbol.register) + ", align 8\n"
                self.instr += 1
                return ("%"+str(self.instr - 1), type[:-1], "reg", currentNode.value)
            if "float*" in type:
                llvmrtyp = symbol.type.replace("float", "float")
                self.llvm += "%" + str(self.instr) + " = load " + llvmrtyp + ", " + llvmrtyp + "* " + str(
                    symbol.register) + ", align 8\n"
                self.instr += 1
                return ("%"+str(self.instr - 1), type[:-1], "reg", currentNode.value)
            if "char*" in type:
                llvmrtyp = symbol.type.replace("char", "i8")
                self.llvm += "%" + str(self.instr) + " = load " + llvmrtyp + ", " + llvmrtyp + "* " + str(
                    symbol.register) + ", align 8\n"
                self.instr += 1
                return ("%"+str(self.instr - 1), type[:-1], "reg", currentNode.value)

            if "int[]" in type:
                llvmtype = type.replace("int", "i32")
                llvmtype = llvmtype.replace("[]", "")
                size = symbol.size
                register = symbol.register
                self.llvm += "%" + str(self.instr) + " = getelementptr inbounds [" + str(
                    size) + " x " + llvmtype + "], [" + str(
                    size) + " x " + llvmtype + "]* " + register + ", i32 0, i32 0" + "\n"
                self.instr += 1
            if "float[]" in type:
                llvmtype = type.replace("float", "float")
                llvmtype = llvmtype.replace("[]", "")
                size = symbol.size
                register = symbol.register
                self.llvm += "%" + str(self.instr) + " = getelementptr inbounds [" + str(
                    size) + " x " + llvmtype + "], [" + str(
                    size) + " x " + llvmtype + "]* " + register + ", i32 0, i32 0" + "\n"
                self.instr += 1
            if "char[]" in type:
                llvmtype = type.replace("char", "i8")
                llvmtype = llvmtype.replace("[]", "")
                size = symbol.size
                register = symbol.register
                self.llvm += "%" + str(self.instr) + " = getelementptr inbounds [" + str(
                    size) + " x " + llvmtype + "], [" + str(
                    size) + " x " + llvmtype + "]* " + register + ", i32 0, i32 0" + "\n"
                self.instr += 1
            return (str(reg), type, "reg", currentNode.value)

    def VisitArrayVariable(self, currentNode):
        #print("ArrayVariable")
        if self.currentTable.lookup(currentNode.value):
            array = self.currentTable.lookup(currentNode.value)
            arraytype = array.type
            var = currentNode.value
            register = array.register
            size = array.size
            if currentNode.index:
                index = currentNode.index.accept(self)

            llvmtype = ""
            if "int" in arraytype:
                llvmtype = arraytype.replace("int", "i32")
                llvmtype = llvmtype.replace("[]", "")
                self.llvm += "%" + str(self.instr) + " = getelementptr inbounds [" + str(
                    size) + " x " + llvmtype + "], [" + str(
                    size) + " x " + llvmtype + "]* " + register + ", i32 0, i32 " + str(
                    index[0]) + "\n"
                self.instr += 1
            elif "float" in arraytype:
                llvmtype = arraytype.replace("float", "float")
                llvmtype = llvmtype.replace("[]", "")
                self.llvm += "%" + str(self.instr) + " = getelementptr inbounds [" + str(
                    size) + " x " + llvmtype + "], [" + str(
                    size) + " x " + llvmtype + "]* " + register + ", i32 0, i32 " + str(
                    index[0]) + "\n"
                self.instr += 1
            elif "char" in arraytype:
                llvmtype = arraytype.replace("char", "i8")
                llvmtype = llvmtype.replace("[]", "")
                self.llvm += "%" + str(self.instr) + " = getelementptr inbounds [" + str(
                    size) + " x " + llvmtype + "], [" + str(
                    size) + " x " + llvmtype + "]* " + register + ", i32 0, i32 " + str(
                    index[0]) + "\n"
                self.instr += 1
            if currentNode.lvalue:
                return ("%"+str(self.instr -1), str(arraytype), "reg", currentNode.value)
            else:
                if arraytype == "int[]":
                    self.llvm += "%" + str(self.instr) + " = load i32, i32* %" + str(
                        self.instr - 1) + ", align 4\n"
                    self.instr += 1
                if arraytype == "float[]":
                    self.llvm += "%" + str(self.instr) + " = load float, float* %" + str(
                        self.instr - 1) + ", align 4\n"
                    self.instr += 1
                if arraytype == "char[]":
                    self.llvm += "%" + str(self.instr) + " = load i8, i8* %" + str(
                        self.instr - 1) + ", align 1\n"
                    self.instr += 1
            return ("%"+str(self.instr-1), str(arraytype), "reg", currentNode.value)
    def VisitBinaryOperation(self, currentNode):
        #print("Binary-----------")
        BinType = None
        children = []
        self.lvalue = False
        storereg = None

        for child in currentNode.children:
            if isinstance(child, Variable):
                symbol = self.currentTable.lookup(child.value)
                if symbol:
                    newType = symbol.type
                if BinType is None:
                    BinType = newType
                elif newType == "float":
                    BinType = newType
                #print("Variable")
            if isinstance(child, Variable):
                newType = self.currentTable.lookup(child.value).type
                if BinType is None:
                    BinType = newType
                elif newType == "float":
                    BinType = newType
                #print("Variable")
            elif isinstance(child, Constant):
                '''
                print("Constant")
                '''
            children.append(child)

        left = currentNode.children[0].accept(self)
        right = currentNode.children[1].accept(self)
        #print("The operands are:")
        print(left)
        print(right)
        lefttype = ""
        righttype = ""
        if not isinstance(currentNode.children[0], Constant):
            lefttype = left[1]
            leftvalue = left[0]
            storereg = leftvalue
        else:
            if righttype == "float":
                lefttype = float(left[0])
            else:
                leftvalue = left[0]
        if not isinstance(currentNode.children[1], Constant):
            var1 = self.currentTable.lookup(currentNode.children[1].value)
            righttype = right[1]
            rightvalue = right[0]
            if not storereg:
                storereg = rightvalue
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
        #print("Binary operator:")
        #print(currentNode.value)
        #print("BinType")
        #print(BinType)
        match currentNode.value:
            case "+":
                if BinType == "int":
                    if isinstance(currentNode.children[1], Constant):
                        self.llvm += "addiu " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        self.llvm += "addiu " + str(storereg) + ", " + str(rightvalue) + ", " + str(leftvalue) + "\n"
                    else:
                        self.llvm += "addu " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(rightvalue)
                    #self.llvm += "%" + str(self.instr) + " = add nsw i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    if left[2] != "reg":
                        try:
                            leftvalue = float(leftvalue)
                        except:
                            print("fail")
                    if right[2] != "reg":
                        try:
                            rightvalue = float(rightvalue)
                        except:
                            print("fail")
                    if isinstance(currentNode.children[1], Constant):
                        packed = struct.pack("f", rightvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        rightvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(rightvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "add.s " + str(storereg) + ", " + str(leftvalue) + ", $f" + str(reg) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        packed = struct.pack("f", leftvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        leftvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(leftvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "add.s " + str(storereg) + ", $f" + str(reg) + ", " + str(rightvalue) + "\n"
                    else:
                        self.llvm += "add.s " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(str(rightvalue))
                    #self.llvm += "%" + str(self.instr) + " = fadd float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
            case "-":
                if BinType == "int":
                    if isinstance(currentNode.children[1], Constant):
                        self.llvm += "addiu " + str(storereg) + ", " + str(leftvalue) + ", " + str(-rightvalue) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        reg = self.FCStack.getFreeTempReg()
                        self.llvm += "addiu $t" + str(reg) + ", $zero, " + str(leftvalue) + "\n"
                        self.FCStack.addTempReg("$t" + str(reg))
                        self.llvm += "subu " + str(storereg) + ", $t" + str(reg) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg("$t" + str(reg))
                    else:
                        self.llvm += "subu " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(rightvalue)
                    #self.llvm += "%" + str(self.instr) + " = sub nsw i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    if left[2] != "reg":
                        try:
                            leftvalue = float(leftvalue)
                        except:
                            print("fail")
                    if right[2] != "reg":
                        try:
                            rightvalue = float(rightvalue)
                        except:
                            print("fail")
                    if isinstance(currentNode.children[1], Constant):
                        packed = struct.pack("f", rightvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        rightvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(rightvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "sub.s " + str(storereg) + ", " + str(leftvalue) + ", $f" + str(reg) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        packed = struct.pack("f", leftvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        leftvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(leftvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "sub.s " + str(storereg) + ", $f" + str(reg) + ", " + str(rightvalue) + "\n"
                    else:
                        self.llvm += "sub.s " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(str(rightvalue))
                    #self.llvm += "%" + str(self.instr) + " = fsub float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
            case "*":
                if BinType == "int":
                    if isinstance(currentNode.children[1], Constant):
                        #reg = self.FCStack.getFreeTempReg()
                        #self.llvm += "addiu $t" + str(reg) + ", $zero, " + str(rightvalue) + "\n"
                        #self.FCStack.addTempReg("$t" + str(reg))
                        self.llvm += "mul " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        #self.FCStack.removeTempReg("$t" + str(reg))
                    elif isinstance(currentNode.children[0], Constant):
                        #reg = self.FCStack.getFreeTempReg()
                        #self.llvm += "addiu $t" + str(reg) + ", $zero, " + str(leftvalue) + "\n"
                        #self.FCStack.addTempReg("$t" + str(reg))
                        self.llvm += "mul " + str(storereg) + ", " + str(rightvalue) + ", " + str(leftvalue) + "\n"
                        #self.FCStack.removeTempReg("$t" + str(reg))
                    else:
                        self.llvm += "mul " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(rightvalue)
                    #self.llvm += "%" + str(self.instr) + " = mul nsw i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    if left[2] != "reg":
                        try:
                            leftvalue = float(leftvalue)
                        except:
                            print("fail")
                    if right[2] != "reg":
                        try:
                            rightvalue = float(rightvalue)
                        except:
                            print("fail")
                    if isinstance(currentNode.children[1], Constant):
                        packed = struct.pack("f", rightvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        rightvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(rightvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "mul.s " + str(storereg) + ", " + str(leftvalue) + ", $f" + str(reg) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        packed = struct.pack("f", leftvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        leftvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(leftvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "mul.s " + str(storereg) + ", $f" + str(reg) + ", " + str(rightvalue) + "\n"
                    else:
                        self.llvm += "mul.s " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(str(rightvalue))
                   #self.llvm += "%" + str(self.instr) + " = fmul float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
            case "/":
                if BinType == "int":
                    if isinstance(currentNode.children[1], Constant):
                        reg = self.FCStack.getFreeTempReg()
                        self.llvm += "addiu $t" + str(reg) + ", $zero, " + str(rightvalue) + "\n"
                        self.FCStack.addTempReg("$t" + str(reg))
                        self.llvm += "div " + str(storereg) + ", " + str(leftvalue) + ", $t" + str(reg) + "\n"
                        self.FCStack.removeTempReg("$t" + str(reg))
                    elif isinstance(currentNode.children[0], Constant):
                        reg = self.FCStack.getFreeTempReg()
                        self.llvm += "addiu $t" + str(reg) + ", $zero, " + str(leftvalue) + "\n"
                        self.FCStack.addTempReg("$t" + str(reg))
                        self.llvm += "div " + str(storereg) + ", $t" + str(reg) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg("$t" + str(reg))
                    else:
                        self.llvm += "div " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(rightvalue)
                    #self.llvm += "%" + str(self.instr) + " = sdiv i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    if left[2] != "reg":
                        try:
                            leftvalue = float(leftvalue)
                        except:
                            print("fail")
                    if right[2] != "reg":
                        try:
                            rightvalue = float(rightvalue)
                        except:
                            print("fail")
                    if isinstance(currentNode.children[1], Constant):
                        packed = struct.pack("f", rightvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        rightvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(rightvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "div.s " + str(storereg) + ", " + str(leftvalue) + ", $f" + str(reg) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        packed = struct.pack("f", leftvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        leftvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(leftvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "div.s " + str(storereg) + ", $f" + str(reg) + ", " + str(rightvalue) + "\n"
                    else:
                        self.llvm += "div.s " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(str(rightvalue))
                    #self.llvm += "%" + str(self.instr) + " = fdiv float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                self.instr += 1
            case "%":
                if BinType == "int":
                    if isinstance(currentNode.children[1], Constant):
                        reg = self.FCStack.getFreeTempReg()
                        self.llvm += "addiu $t" + str(reg) + ", $zero, " + str(rightvalue) + "\n"
                        self.FCStack.addTempReg("$t" + str(reg))
                        self.llvm += "div " + str(storereg) + ", " + str(leftvalue) + ", $t" + str(reg) + "\n"
                        self.FCStack.removeTempReg("$t" + str(reg))
                        self.llvm += "mfhi " + str(storereg) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        reg = self.FCStack.getFreeTempReg()
                        self.llvm += "addiu $t" + str(reg) + ", $zero, " + str(leftvalue) + "\n"
                        self.FCStack.addTempReg("$t" + str(reg))
                        self.llvm += "div " + str(storereg) + ", $t" + str(reg) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg("$t" + str(reg))
                        self.llvm += "mfhi " + str(storereg) + "\n"
                    else:
                        self.llvm += "div " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(rightvalue)
                        self.llvm += "mfhi " + str(storereg) + "\n"
                    #self.llvm += "%" + str(self.instr) + " = srem i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    if left[2] != "reg":
                        try:
                            leftvalue = float(leftvalue)
                        except:
                            print("fail")
                    if right[2] != "reg":
                        try:
                            rightvalue = float(rightvalue)
                        except:
                            print("fail")
                    #self.llvm += "%" + str(self.instr) + " = frem float " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                #self.instr += 1
            case "==":
                if BinType == "int":
                    if isinstance(currentNode.children[0], Constant):
                        self.llvm += "seq " + str(storereg) + ", " + str(rightvalue) + ", " + str(leftvalue) + "\n"
                    else:
                        self.llvm += "seq " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(leftvalue)
                    #self.llvm += "%" + str(self.instr) + " = icmp eq i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    if left[2] != "reg":
                        try:
                            leftvalue = float(leftvalue)
                        except:
                            print("fail")
                    if right[2] != "reg":
                        try:
                            rightvalue = float(rightvalue)
                        except:
                            print("fail")
                    if isinstance(currentNode.children[1], Constant):
                        packed = struct.pack("f", rightvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        rightvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(rightvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.eq.s " + str(leftvalue) + ", $f" + str(reg) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        packed = struct.pack("f", leftvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        leftvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(leftvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.eq.s $f" + str(reg) + ", " + str(
                            rightvalue) + "\n"
                    else:
                        self.llvm += "c.eq.s " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(str(rightvalue))
                    reg = self.FCStack.getFreeTempReg()
                    self.llvm += "li $at, 0 \n"
                    self.llvm += "li $at, 1\n"
                    self.llvm += "movt $t" + str(reg) + ", $at\n"
                    self.FCStack.addTempReg("$t" + str(reg))
                return ("$t"+str(reg), BinType, "bool", "", "value")
            case "<":
                if BinType == "int":
                    if isinstance(currentNode.children[0], Constant):
                        self.llvm += "slti " + str(storereg) + ", " + str(rightvalue) + ", " + str(leftvalue) + "\n"
                    elif isinstance(currentNode.children[1], Constant):
                        self.llvm += "slti " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                    else:
                        self.llvm += "slt " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(leftvalue)
                    #self.llvm += "%" + str(self.instr) + " = icmp eq i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    if left[2] != "reg":
                        try:
                            leftvalue = float(leftvalue)
                        except:
                            print("fail")
                    if right[2] != "reg":
                        try:
                            rightvalue = float(rightvalue)
                        except:
                            print("fail")
                    if isinstance(currentNode.children[1], Constant):
                        packed = struct.pack("f", rightvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        rightvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(rightvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.lt.s " + str(leftvalue) + ", $f" + str(reg) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        packed = struct.pack("f", leftvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        leftvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(leftvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.lt.s $f" + str(reg) + ", " + str(
                            rightvalue) + "\n"
                    else:
                        self.llvm += "c.lt.s " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(str(rightvalue))
                    reg = self.FCStack.getFreeTempReg()
                    self.llvm += "li $at, 0 \n"
                    self.llvm += "li $at, 1\n"
                    self.llvm += "movt $t" + str(reg) + ", $at\n"
                    self.FCStack.addTempReg("$t" + str(reg))
                return ("$t" + str(reg), BinType, "bool", "", "value")
            case "<=":
                if BinType == "int":
                    if isinstance(currentNode.children[0], Constant):
                        self.llvm += "sle " + str(storereg) + ", " + str(rightvalue) + ", " + str(leftvalue) + "\n"
                    elif isinstance(currentNode.children[1], Constant):
                        self.llvm += "sle " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                    else:
                        self.llvm += "sle " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(leftvalue)
                    #self.llvm += "%" + str(self.instr) + " = icmp eq i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    if left[2] != "reg":
                        try:
                            leftvalue = float(leftvalue)
                        except:
                            print("fail")
                    if right[2] != "reg":
                        try:
                            rightvalue = float(rightvalue)
                        except:
                            print("fail")
                    if isinstance(currentNode.children[1], Constant):
                        packed = struct.pack("f", rightvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        rightvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(rightvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.le.s " + str(leftvalue) + ", $f" + str(reg) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        packed = struct.pack("f", leftvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        leftvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(leftvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.le.s $f" + str(reg) + ", " + str(
                            rightvalue) + "\n"
                    else:
                        self.llvm += "c.le.s " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(str(rightvalue))
                    reg = self.FCStack.getFreeTempReg()
                    self.llvm += "li $at, 0 \n"
                    self.llvm += "li $at, 1\n"
                    self.llvm += "movt $t" + str(reg) + ", $at\n"
                    self.FCStack.addTempReg("$t" + str(reg))
                return ("$t" + str(reg), BinType, "bool", "", "value")
            case ">":
                if BinType == "int":
                    if isinstance(currentNode.children[0], Constant):
                        self.llvm += "sgti " + str(storereg) + ", " + str(rightvalue) + ", " + str(leftvalue) + "\n"
                    elif isinstance(currentNode.children[1], Constant):
                        self.llvm += "sgti " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                    else:
                        self.llvm += "sgt " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(leftvalue)
                    #self.llvm += "%" + str(self.instr) + " = icmp eq i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    if left[2] != "reg":
                        try:
                            leftvalue = float(leftvalue)
                        except:
                            print("fail")
                    if right[2] != "reg":
                        try:
                            rightvalue = float(rightvalue)
                        except:
                            print("fail")
                    if isinstance(currentNode.children[1], Constant):
                        packed = struct.pack("f", rightvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        rightvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(rightvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.lt.s $f" + str(reg) + ", " + str(leftvalue) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        packed = struct.pack("f", leftvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        leftvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(leftvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.lt.s " + str(rightvalue) + ", $f" + str(
                            reg) + "\n"
                    else:
                        self.llvm += "c.lt.s " + str(rightvalue) + ", " + str(leftvalue) + "\n"
                        self.FCStack.removeTempReg(str(leftvalue))
                    reg = self.FCStack.getFreeTempReg()
                    self.llvm += "li $at, 0 \n"
                    self.llvm += "li $at, 1\n"
                    self.llvm += "movt $t" + str(reg) + ", $at\n"
                    self.FCStack.addTempReg("$t" + str(reg))
                return ("$t" + str(reg), BinType, "bool", "", "value")
            case ">=":
                if BinType == "int":
                    if isinstance(currentNode.children[0], Constant):
                        self.llvm += "sge " + str(storereg) + ", " + str(rightvalue) + ", " + str(leftvalue) + "\n"
                    elif isinstance(currentNode.children[1], Constant):
                        self.llvm += "sge " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                    else:
                        self.llvm += "sge " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(leftvalue)
                    #self.llvm += "%" + str(self.instr) + " = icmp eq i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    if left[2] != "reg":
                        try:
                            leftvalue = float(leftvalue)
                        except:
                            print("fail")
                    if right[2] != "reg":
                        try:
                            rightvalue = float(rightvalue)
                        except:
                            print("fail")
                    if isinstance(currentNode.children[1], Constant):
                        packed = struct.pack("f", rightvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        rightvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(rightvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.le.s $f" + str(reg) + ", " + str(leftvalue) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        packed = struct.pack("f", leftvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        leftvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(leftvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.le.s " + str(rightvalue) + ", $f" + str(
                            reg) + "\n"
                    else:
                        self.llvm += "c.le.s " + str(rightvalue) + ", " + str(leftvalue) + "\n"
                        self.FCStack.removeTempReg(str(rightvalue))
                    reg = self.FCStack.getFreeTempReg()
                    self.llvm += "li $at, 0 \n"
                    self.llvm += "li $at, 1\n"
                    self.llvm += "movt $t" + str(reg) + ", $at\n"
                    self.FCStack.addTempReg("$t" + str(reg))
                return ("$t" + str(reg), BinType, "bool", "", "value")
            case "!=":
                if BinType == "int":
                    if isinstance(currentNode.children[0], Constant):
                        self.llvm += "sne " + str(storereg) + ", " + str(rightvalue) + ", " + str(leftvalue) + "\n"
                    else:
                        self.llvm += "sne " + str(storereg) + ", " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(leftvalue)
                    #self.llvm += "%" + str(self.instr) + " = icmp eq i32 " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                elif BinType == "float":
                    if left[2] != "reg":
                        try:
                            leftvalue = float(leftvalue)
                        except:
                            print("fail")
                    if right[2] != "reg":
                        try:
                            rightvalue = float(rightvalue)
                        except:
                            print("fail")
                    if isinstance(currentNode.children[1], Constant):
                        packed = struct.pack("f", rightvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        rightvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(rightvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.eq.s " + str(leftvalue) + ", $f" + str(reg) + "\n"
                    elif isinstance(currentNode.children[0], Constant):
                        packed = struct.pack("f", leftvalue)
                        unpacked = struct.unpack("<I", packed)[0]
                        leftvalue = hex(unpacked)
                        self.llvm += "li $at, " + str(leftvalue) + "\n"
                        reg = self.FCStack.getFreeFTempReg()
                        self.llvm += "mtc1 $at, $f" + str(reg) + "\n"
                        self.llvm += "c.eq.s $f" + str(reg) + ", " + str(
                            rightvalue) + "\n"
                    else:
                        self.llvm += "c.eq.s " + str(leftvalue) + ", " + str(rightvalue) + "\n"
                        self.FCStack.removeTempReg(str(rightvalue))
                    reg = self.FCStack.getFreeTempReg()
                    self.llvm += "li $at, 0 \n"
                    self.llvm += "li $at, 1\n"
                    self.llvm += "movf $t" + str(reg) + ", $at\n"
                    self.FCStack.addTempReg("$t" + str(reg))
                return ("$t" + str(reg), BinType, "bool", "", "value")


        return (storereg, BinType, "reg", "", "value")

    def VisitUnaryOperation(self, currentNode):
        #print("Unary")
        match currentNode.value:
            case "&":
                self.lvalue = True
                print(currentNode.children[0])
                node = currentNode.children[0].accept(self)
                node = (node[0], "address", node[2], node[3])
                print(node)
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
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* " + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                elif "float*" in var[1]:
                                    llvmrtyp = var[1].replace("float", "float")
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* " + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                else:
                                    llvmrtyp = var[1].replace("char", "i8")
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* " + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                # INT OOG HOUDE
                                var = ("%" + str(self.instr-1), str(variable.type), "reg", currentNode.value)
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
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* " + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                elif "float*" in var[1]:
                                    llvmrtyp = var[1].replace("float", "float")
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* " + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                else:
                                    llvmrtyp = var[1].replace("char", "i8")
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* " + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                var = ("%"+ str(self.instr-1), str(variable.type[:-1]), "reg", var[3])

                            else:
                                var = child.accept(self)
                                llvmrtyp = var[1].replace("int", "i32")
                                if "int*" in var[1]:
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* " + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                elif "float*" in var[1]:
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* " + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                else:
                                    self.llvm += "%" + str(self.instr) + " = load " + str(llvmrtyp) + ", " + str(llvmrtyp) + "* " + str(var[0]) + ", align 8\n"
                                    self.instr += 1
                                var = ("%" + str(self.instr-1), str(var[1][:-1]), "reg", var[3])
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
                    var = ("%" + str(self.instr - 1), str(var[1]), "reg", var[3])
                    return var
                else:
                    return var

            case "++":
                #print("DOING THISIIII")
                for child in currentNode.children:
                    #print(child)
                    if isinstance(child, Variable) or isinstance(child, ArrayVariable):
                        var = self.currentTable.lookup(child.value)
                        match var.type:
                            case "int":
                                self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(var.register) + ", align 4\n"
                                self.instr += 1
                                self.llvm += "%" + str(self.instr) + " = add nsw i32 %" + str(self.instr-1) + ", 1\n"
                                self.instr += 1
                                self.llvm += "store i32 %" + str(self.instr-1) + ", i32* " + str(var.register) + ", align 4\n"
                                return ("%"+str(self.instr-2) , str(var.type), "reg", str(child.value))
                            case "float":
                                self.llvm += "%" + str(self.instr) + " = load float, float* " + str(var.register) + ", align 4\n"
                                self.instr += 1
                                self.llvm += "%" + str(self.instr) + " = fadd float %" + str(self.instr-1) + ", 1.0\n"
                                self.instr += 1
                                self.llvm += "store float %" + str(self.instr-1) + ", float* " + str(var.register) + ", align 4\n"
                                return ("%"+str(self.instr-2) , str(var.type), "reg", str(child.value))
                        if "int[]" in var.type:
                            value = child.accept(self)
                            self.llvm += "%" + str(self.instr) + " = add nsw i32 " + str(value[0]) + ", 1\n"
                            self.instr += 1
                            self.llvm += "store i32 %" + str(self.instr - 1) + ", i32* " + str(
                                int(value[0])-1) + ", align 4\n"
                            return ("%"+str(int(value[0])), str(var.type), "reg", str(child.value))
                    else:
                        node = child.accept(self)
                        #print(node)
                        if "int" in node[1]:
                            self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(node[0]) + ", align 4\n"
                            self.instr += 1
                            self.llvm += "%" + str(self.instr) + " = add nsw i32 %" + str(self.instr - 1) + ", 1\n"
                            self.instr += 1
                            self.llvm += "store i32 %" + str(self.instr - 1) + ", i32* %" + str(self.instr - 3) + ", align 4\n"
                            return ("%" + str(self.instr - 3), '', "reg", str(child.value))
                        elif "float" in node[1]:
                            self.llvm += "%" + str(self.instr) + " = load float, float* " + str(node[0]) + ", align 4\n"
                            self.instr += 1
                            self.llvm += "%" + str(self.instr) + " = fadd float %" + str(self.instr - 1) + ", 1.0\n"
                            self.instr += 1
                            self.llvm += "store float %" + str(self.instr - 1) + ", float* %" + str(
                                self.instr - 3) + ", align 4\n"
                            return ("%" + str(self.instr - 3), '', "reg", str(child.value))

            case "--":
                for child in currentNode.children:
                    if isinstance(child, Variable):
                        var = self.currentTable.lookup(child.value)
                        match var.type:
                            case "int":
                                self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(var.register) + ", align 4\n"
                                self.instr += 1
                                self.llvm += "%" + str(self.instr) + " = sub nsw i32 %" + str(self.instr-1) + ", 1\n"
                                self.instr += 1
                                self.llvm += "store i32 %" + str(self.instr-1) + ", i32* " + str(var.register) + ", align 4\n"
                                return ("%"+str(self.instr-2) , str(var.type), "reg", str(child.value))
            case "-":
                print("Unary -")
                for child in currentNode.children:
                    node = child.accept(self)
                    print("node")
                    print(node)
                    if isinstance(node, Variable) or isinstance(node, ArrayVariable):
                        var = self.currentTable.lookup(child.value)
                        print(var)
                        match var.type:
                            case "int":
                                '''
                                self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(var.register) + ", align 4\n"
                                self.instr += 1
                                self.llvm += "%" + str(self.instr) + " = sub nsw i32 0 , %" + str(self.instr-1) + "\n"
                                self.instr += 1
                                '''
                                reg = self.FCStack.getFreeFTempReg()
                                print(reg)
                                self.llvm += "lw $" + str(reg) + ", " + str(var.register) + "($fp) \n"
                                self.llvm += "negu $" + str(reg) + ", $" + str(reg) + "\n"
                                return ("$" + str(reg) , str(var.type), "reg", str(child.value))
                            case "float":
                                '''
                                self.llvm += "%" + str(self.instr) + " = load float, float* " + str(var.register) + ", align 4\n"
                                self.instr += 1
                                self.llvm += "%" + str(self.instr) + " = fneg float %" + str(self.instr-1) + "\n"
                                self.instr += 1
                                return ("%"+str(self.instr-1) , str(var.type), "reg", str(child.value))
                                '''
                                reg = self.FCStack.getFreeFTempReg()
                                print(reg)
                                self.llvm += "lw $" + str(reg) + ", " + str(var.register) + "($fp) \n"
                                self.llvm += "negu $" + str(reg) + ", $" + str(reg) + "\n"
                                return ("$" + str(reg), str(var.type), "reg", str(child.value))
                        if "int[]" in var.type:
                            value = child.accept(self)
                            self.llvm += "%" + str(self.instr) + " = add nsw i32 " + str(value[0]) + ", 1\n"
                            self.instr += 1
                            self.llvm += "store i32 %" + str(self.instr - 1) + ", i32* " + str(
                                int(value[0])-1) + ", align 4\n"
                            return ("%"+str(int(value[0])), str(var.type), "reg", str(child.value))
                    else:
                        #print("DEEES DAN?")
                        match node[1]:
                            case "int":
                                #self.llvm += "%" + str(self.instr) + " = sub nsw i32 0 , %" + str(self.instr-1) + "\n"
                                #self.instr += 1
                                self.llvm += "negu " + str(node[0]) + ", " + str(node[0]) + "\n"
                                return (str(node[0]) , str(node[1]), "reg", str(child.value))
                                #print("RETURN")
                                #return ("%"+str(self.instr-1) , str(node[1]), "reg", str(child.value))
                            case "float":
                                '''
                                self.llvm += "%" + str(self.instr) + " = fneg float %" + str(self.instr-1) + "\n"
                                self.instr += 1
                                return ("%"+str(self.instr-1) , str(node[1]), "reg", str(child.value))
                                '''
                                reg = self.FCStack.getFreeFTempReg()
                                print(reg)
                                self.llvm += "mtc1 $zero, $f" + str(reg) + "\n"
                                self.llvm += "sub.s " + str(node[0]) + ", $f" + str(reg) + ", " + str(node[0]) + "\n"
                                return (str(node[0]), str(node[1]), "reg", str(child.value))

            case "!":
                for child in currentNode.children:
                    if isinstance(child, Variable) or isinstance(child, ArrayVariable):
                        var = self.currentTable.lookup(child.value)
                        match var.type:
                            case "int":
                                self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(var.register) + ", align 4\n"
                                self.instr += 1
                                self.llvm += "%" + str(self.instr) + " = sub nsw i32 1 , %" + str(self.instr-1) + "\n"
                                self.instr += 1
                                return ("%"+str(self.instr-1) , str(var.type), "reg", str(child.value))
                            case "float":
                                self.llvm += "%" + str(self.instr) + " = load float, float* " + str(var.register) + ", align 4\n"
                                self.instr += 1
                                self.llvm += "%" + str(self.instr) + " = fneg float %" + str(self.instr-1) + "\n"
                                self.instr += 1
                                return ("%"+str(self.instr-1) , str(var.type), "reg", str(child.value))
                        if "int[]" in var.type:
                            value = child.accept(self)
                            self.llvm += "%" + str(self.instr) + " = add nsw i32 " + str(value[0]) + ", 1\n"
                            self.instr += 1
                            self.llvm += "store i32 %" + str(self.instr - 1) + ", i32* " + str(
                                int(value[0])-1) + ", align 4\n"
                            return ("%"+str(int(value[0])), str(var.type), "reg", str(child.value))

            case "[]":
                #print(len(currentNode.children))
                #print(currentNode.children)
                #print(currentNode.children[0].value)
                #print(currentNode.value)
                if self.lvalue:
                    if currentNode.children:
                        for child in currentNode.children:
                            '''
                            print(child)
                            print(child.children[0])
                            '''
            case other:
                print("not implemented yet")
        return currentNode

    def VisitArray(self, currentNode):
        #print("Array")
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

        # If we are assigning in global scope
        if self.currentTable.name == "Global":

            # For a global variable, allocate them and value them 0 if not assigned

            ltype = currentNode.type
            var = currentNode.var
            value = ("0", "", "value")
            symbol = self.currentTable.lookupUnallocated(var)
            #print(symbol.type)
            ltype = symbol.type

            # Test for type
            if "[]" in symbol.type:
                if "int" in ltype:
                    vartype = ltype.replace("int", "i32")
                    vartype = vartype.replace("[]","")
                    self.llvm += "@" + str(var) + " = dso_local global [" + str(symbol.size) + " x " + str(vartype) + "] zeroinitializer, align 16\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "float" in ltype:
                    vartype = ltype.replace("float", "float")
                    vartype = vartype.replace("[]", "")
                    self.llvm += "@" + str(var) + " = dso_local global [" + str(symbol.size) + " x " + str(vartype) + "] zeroinitializer, align 16\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "char" in ltype:
                    vartype = ltype.replace("char", "i8")
                    vartype = vartype.replace("[]", "")
                    self.llvm += "@" + str(var) + " = dso_local global [" + str(symbol.size) + " x " + str(vartype) + "] zeroinitializer, align 16\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
            elif "*" in symbol.type:
                if "int" in ltype:
                    vartype = ltype.replace("int", "i32")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str("null") + ", align 8\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "float" in ltype:
                    vartype = ltype.replace("float", "float")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str("null") + ", align 8\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "char" in ltype:
                    vartype = ltype.replace("char", "i8")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str("null") + ", align 8\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
            else:
                if "int" in ltype:
                    try:
                        value = int(value[0])
                    except ValueError:
                        print("Cannot be converted")
                    vartype = ltype.replace("int", "i32")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str(value) + ", align 4\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "float" in ltype:
                    try:
                        value = float(value[0])
                    except ValueError:
                        print("Cannot be converted")
                    packed = struct.pack("f", value)
                    unpacked = struct.unpack("f", packed)[0]
                    vartype = ltype.replace("float", "float")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str(value) + ", align 4\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "char" in ltype:
                    vartype = ltype.replace("char", "i8")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str("0") + ", align 1\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
        else:
            var = currentNode.var
            node = self.currentTable.lookupUnallocated(var)
            #self.allocateRegister(self.currentTable, var, node)
            self.allocateRegister(self.currentTable, var, node)
            context = self.FCStack.peek()
            context.offset -= 4
        return currentNode

    def VisitAssignment(self, currentNode):
        #print("Assignment2LLVM")
        if self.currentTable.name == "Global":

            # For a global variable, allocate them and value them 0 if not assigned
            ltype = currentNode.lvalue.type
            var = currentNode.lvalue.var
            value = ("0", "", "value")
            symbol = self.currentTable.lookupUnallocated(var)
            ltype = symbol.type
            self.lvalue = False
            value = currentNode.rvalue.accept(self)
            self.lvalue = True
            # Test for type
            '''
            if "[]" in symbol.type:
                if "int" in ltype:
                    vartype = ltype.replace("int", "i32")
                    vartype = vartype.replace("[]","")
                    self.llvm += "@" + str(var) + " = dso_local global [" + str(symbol.size) + " x " + str(vartype) + "] zeroinitializer, align 16\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "float" in ltype:
                    vartype = ltype.replace("float", "float")
                    vartype = vartype.replace("[]", "")
                    self.llvm += "@" + str(var) + " = dso_local global [" + str(symbol.size) + " x " + str(vartype) + "] zeroinitializer, align 16\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "char" in ltype:
                    vartype = ltype.replace("char", "i8")
                    vartype = vartype.replace("[]", "")
                    self.llvm += "@" + str(var) + " = dso_local global [" + str(symbol.size) + " x " + str(vartype) + "] zeroinitializer, align 16\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
            '''
            if "*" in symbol.type:
                if "int" in ltype:
                    vartype = ltype.replace("int", "i32")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str(value[0]) + ", align 8\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "float" in ltype:
                    vartype = ltype.replace("float", "float")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str(value[0]) + ", align 8\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "char" in ltype:
                    vartype = ltype.replace("char", "i8")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str(value[0]) + ", align 8\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
            else:
                if "int" in ltype:
                    try:
                        value = int(value[0])
                    except ValueError:
                        print("Cannot be converted")
                    vartype = ltype.replace("int", "i32")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str(value) + ", align 4\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "float" in ltype:
                    try:
                        value = float(value[0])
                    except ValueError:
                        print("Cannot be converted")
                    packed = struct.pack("f", value)
                    unpacked = struct.unpack("f", packed)[0]
                    vartype = ltype.replace("float", "float")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str(value) + ", align 4\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
                elif "char" in ltype:
                    value = value[0].replace("'", "")
                    if len(value[0]) > 1:
                        value = value[0].encode('utf-8').decode('unicode-escape')
                    vartype = ltype.replace("char", "i8")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str("0") + ", align 1\n"
                    self.currentTable.insertRegister(var, "@"+str(var))
            '''
            # If we are assigning in global scope
            if self.currentTable.name == "Global":
                # For a global variable, allocate them and value them 0 if not assigned
                ltype = currentNode.lvalue.type
                var = currentNode.lvalue.var
                value = ("0", "", "value")
                self.lvalue = False
                value = currentNode.rvalue.accept(self)
                self.lvalue = True
                if "int" in ltype:
                    try:
                        value = int(value[0])
                    except ValueError:
                        print("Cannot be converted")
                    vartype = ltype.replace("int", "i32")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str(value) + ", align 4\n"
                elif "float" in ltype:
                    try:
                        value = float(value[0])
                    except ValueError:
                        print("Cannot be converted")
                    packed = struct.pack("f", value)
                    unpacked = struct.unpack("f", packed)[0]
                    vartype = ltype.replace("float", "float")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str(value) + ", align 4\n"
                elif "char" in ltype:
                    value = value[0].replace("'", "")
                    if len(value[0]) > 1:
                        value = value[0].encode('utf-8').decode('unicode-escape')
                    vartype = ltype.replace("char", "i8")
                    self.llvm += "@" + str(var) + " = dso_local global " + str(vartype) + " " + str(ord(value)) + ", align 1\n"
            '''

        else:
            # Test if the left value is a declaration
            if isinstance(currentNode.lvalue, Declaration):
                context = self.FCStack.peek()
                print("Before assigning context offset is:" + str(context.offset))
                # context.offset -= 4
                currentNode.lvalue.accept(self)
                context = self.FCStack.peek()
                print("First after assigning context offset is:" + str(context.offset))
                self.lvalue = False
                value = currentNode.rvalue.accept(self)
                self.lvalue = True
                print(value)
                node = self.currentTable.lookupUnallocated(currentNode.lvalue.var)
                #print("What is the node")
                #print(node)
                #self.allocateRegister(self.currentTable, currentNode.lvalue.var, node)
                print(value)
                print("Decl")
                symbol = self.currentTable.lookup(currentNode.lvalue.var)
                print(symbol.register)
                ltype = self.currentTable.lookup(currentNode.lvalue.var).type
                if value[1] == "address":
                    self.llvm += "addiu $at, $fp, " + str(value[0]) + " \n"
                    #context = self.FCStack.peek()
                    self.llvm += "sw $at, " + str(symbol.register) + "($sp) \n"

                elif value[2] != "reg":
                    if ltype == "int":
                        try:
                            value = int(value[0])
                        except ValueError:
                            value = float(value[0])
                        if isinstance(value, float) or isinstance(value, int):
                            print(value)
                            print("here")
                            #self.llvm += "store i32 " + str(value) + ", i32* " + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 4\n"
                            self.llvm += "addiu $at, $zero, " + str(value) + " \n"
                            context = self.FCStack.peek()
                            self.llvm += "sw $at, " + str(symbol.register) + "($sp) \n"
                            #context.offset -= 4
                            print("After assigning context offset is:" + str(context.offset))
                    elif ltype == "float":
                        try:
                            value = float(value[0])
                        except ValueError:
                            print("failiure")
                        packed = struct.pack("f", value)
                        unpacked = struct.unpack("<I", packed)[0]
                        print(hex(unpacked))
                        self.llvm += "li $at, " + str(hex(unpacked)) + "\n"
                        #context = self.FCStack.peek()
                        self.llvm += "sw $at, " + str(symbol.register) + "($sp) \n"
                        #context.offset -= 4
                        #self.llvm += "store float " + str(unpacked) + ", float* " + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                    elif ltype == "char":
                        value = value[0].replace("'", "")
                        if len(value) > 1:
                            value= value.encode('utf-8').decode('unicode-escape')
                        self.llvm += "li $at, " + str(ord(value)) + "\n"
                        #context = self.FCStack.peek()
                        self.llvm += "sw $at, " + str(symbol.register) + "($sp) \n"
                        #context.offset -= 4
                        #self.llvm += "store i8 " + str(ord(value)) + ", i8* " + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 1\n"
                    elif ltype == "int*":
                        print("Address??")
                        self.llvm += "store i32* " + str(value) + ", i32** " + self.currentTable.lookup(
                            currentNode.lvalue.var).register + ", align 8\n"
                    elif ltype == "float*":
                        self.llvm += "store float* " + str(value) + ", float** " + self.currentTable.lookup(
                            currentNode.lvalue.var).register + ", align 8\n"
                    elif ltype == "char*":
                        self.llvm += "store i8* " + str(value) + ", i8** " + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 8\n"
                else:
                    if ltype == "int":
                        '''
                        if value[1] == "float":
                            self.llvm += "%" + str(self.instr) + " = fptosi float " + str(value[0]) + " to i32\n"
                            self.instr += 1
                        self.llvm += "store i32 %" + str(self.instr-1) + ", i32* " + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                        '''

                        print(value)
                        # self.llvm += "store i32 " + str(value) + ", i32* " + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 4\n"
                        context = self.FCStack.peek()
                        self.llvm += "sw " + value[0] + ", " + str(symbol.register) + "($sp) \n"
                        #context.offset -= 4
                        print("After assigning context offset is:" + str(context.offset))
                        self.FCStack.removeTempReg(value[0])
                    elif ltype == "float":
                        if value[1] == "int":
                            self.llvm += "%" + str(self.instr) + " = sitofp i32 " + str(value[0]) + " to float\n"
                            self.instr += 1
                        context = self.FCStack.peek()
                        self.llvm += "swc1 " + value[0] + ", " + str(symbol.register) + "($sp) \n"
                        #context.offset -= 4
                        self.FCStack.removeTempReg(value[0])
                        #self.llvm += "store float %" + str(self.instr-1) + ", float* " + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                    elif ltype == "char":
                        context = self.FCStack.peek()
                        self.llvm += "sw " + value[0] + ", " + str(symbol.register) + "($sp) \n"
                        #context.offset -= 4
                        self.FCStack.removeTempReg(value[0])
                        #self.llvm += "store i8 " + str(value[0]) + ", i8* " + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 1\n"
                    elif "int*" == ltype:
                        print("ja??")
                        print(ltype)
                        self.llvm += "store i32* " + str(value[0]) + ", i32** " + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 8\n"
                    elif "float*" == ltype:
                        self.llvm += "store float* " + str(value[0]) + ", float** " + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 8\n"
                    elif "char*" == ltype:
                        self.llvm += "store i8* " + str(value[0]) + ", i8** " + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 1\n"
                    elif "int*" in ltype:
                        print("Address here??")
                        # We need to dereference more
                        if ltype != value[1]:
                            llvmltyp = ltype.replace("int", "i32")
                            llvmrtyp = value[1].replace("int", "i32")
                            self.llvm += "store "+ str(llvmrtyp) + "* " + str(value[0]) + ", " + str(llvmltyp) + "* " + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 8\n"
                        else:
                            llvmltyp = ltype.replace("int", "i32")
                            llvmrtyp = value[1].replace("int", "i32")
                            self.llvm += "store " + str(llvmrtyp) + "* " + str(value[0]) + ", " + str(
                                llvmltyp) + "* " + str(
                                self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 8\n"

                    elif "int*" in ltype:
                        # We need to dereference more
                        self.llvm += "store float* " + str(value[0]) + ", float** " + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 8\n"
                    elif "int*" in ltype:
                        # We need to dereference more
                        self.llvm += "store i8* " + str(value[0]) + ", i8** " + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 1\n"
                    else:
                        '''
                        print("test")
                        '''
                self.currentTable.lookup(currentNode.lvalue.var).inUse = True

            # The lvalue is no declaration but a variable
            elif isinstance(currentNode.lvalue, Variable) or isinstance(currentNode.lvalue, ArrayVariable):
                self.lvalue = False
                value = currentNode.rvalue.accept(self)
                self.lvalue = True
                reg = currentNode.lvalue.accept(self)
                #print("REG:")
                #print(reg)
                #print("Value")
                #print(value)
                #ltype = self.symbolTable.lookup(currentNode.lvalue.children[0].value).type
                symbol = self.currentTable.lookup(currentNode.lvalue.value)
                ltype = self.currentTable.lookup(currentNode.lvalue.value).type
                #print(ltype)
                #self.instr += 1
                '''
                if ltype == "int*":
                    self.llvm += "store i32* " + str(value[0]) + ", i32** " + str(reg[0]) + ", align 8\n"
                if ltype == "float*":
                    self.llvm += "store float* " + str(value[0]) + ", float** " + str(reg[0]) + ", align 8\n"
                if ltype == "char*":
                    self.llvm += "store i8* " + str(value[0]) + ", i8** " + str(reg[0]) + ", align 1\n"
                '''

                if value[1] == "address":
                    self.llvm += "addiu $at, $fp, " + str(value[0]) + " \n"
                    context = self.FCStack.peek()
                    self.llvm += "sw $at, " + str(reg[0]) + "($sp) \n"
                elif value[2] != "reg":
                    if ltype == "int":
                        try:
                            value = int(value[0])
                        except ValueError:
                            value = float(value[0])
                        if isinstance(value, float) or isinstance(value, int):
                            print(value)
                            #self.llvm += "store i32 " + str(value) + ", i32* " + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 4\n"
                            self.llvm += "addiu $at, $zero, " + str(value) + " \n"
                            context = self.FCStack.peek()
                            self.llvm += "sw $at, " + str(reg[0]) + "($sp) \n"
                    elif ltype == "float":
                        try:
                            value = float(value[0])
                        except ValueError:
                            print("failiure")
                        packed = struct.pack("f", value)
                        unpacked = struct.unpack("<I", packed)[0]
                        print(hex(unpacked))
                        self.llvm += "li $at, " + str(hex(unpacked)) + "\n"
                        context = self.FCStack.peek()
                        self.llvm += "sw $at, " + str(reg[0]) + "($sp) \n"
                        #self.llvm += "store float " + str(unpacked) + ", float* " + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                    elif ltype == "char":
                        value = value[0].replace("'", "")
                        if len(value) > 1:
                            value= value.encode('utf-8').decode('unicode-escape')
                        self.llvm += "li $at, " + str(ord(value)) + "\n"
                        context = self.FCStack.peek()
                        self.llvm += "sw $at, " + str(reg[0]) + "($sp) \n"
                    if ltype == "int[]":
                        llvmtype = ltype.replace("int", "i32")
                        llvmtype = llvmtype.replace("[]", "")
                        try:
                            value = int(value[0])
                        except ValueError:
                            value = float(value[0])
                        self.llvm += "store i32 " + str(value) + ", i32* %" + str(self.instr - 1) + ", align 4\n"
                    elif ltype == "float[]":
                        llvmtype = ltype.replace("float", "float")
                        llvmtype = llvmtype.replace("[]", "")
                        try:
                            value = float(value[0])
                        except ValueError:
                            print("failiure")
                        packed = struct.pack("f", value)
                        value = struct.unpack("f", packed)[0]
                        self.llvm += "store float " + str(value) + ", float* %" + str(self.instr - 1) + ", align 4\n"
                    elif ltype == "char[]":
                        #print("Zitten we ier?")
                        llvmtype = ltype.replace("char", "i8")
                        llvmtype = llvmtype.replace("[]", "")
                        value = value[0].replace("'","")
                        if len(value) > 1:
                            value = value.encode('utf-8').decode('unicode-escape')
                        self.llvm += "store i8 " + str(ord(value)) + ", i8* %" + str(self.instr - 1) + ", align 4\n"
                    if "[]" in ltype:
                        '''
                        print("KOMETEM IER?")
                        var = reg[3]
                        register = reg[0]
                        symbol = self.currentTable.lookup(var)
                        size = symbol.size
                        index = currentNode.lvalue.size
                        llvmtype = ""
                        if "int" in ltype:
                            llvmtype = ltype.replace("int", "i32")
                            llvmtype = llvmtype.replace("[]", "")
                            try:
                                value = int(value[0])
                            except ValueError:
                                value = float(value[0])
                            self.llvm += "%" + str(self.instr) + " = getelementptr inbounds [" + str(
                                size) + " x " + llvmtype + "], [" + str(
                                size) + " x " + llvmtype + "]* %" + register + ", i64 0, i64 " + str(
                                index) + "\n"
                            self.instr += 1
                            self.llvm += "store i32 " + str(value) + ", i32* %" + str(self.instr-1) + ", align 4\n"
                        elif "float" in ltype:
                            llvmtype = ltype.replace("float", "float")
                            llvmtype = llvmtype.replace("[]", "")
                            try:
                                value = float(value[0])
                            except ValueError:
                                print("failiure")
                            packed = struct.pack("f", value)
                            value = struct.unpack("f", packed)[0]
                            self.llvm += "%" + str(self.instr) + " = getelementptr inbounds [" + str(
                                size) + " x " + llvmtype + "], [" + str(
                                size) + " x " + llvmtype + "]* %" + register + ", i64 0, i64 " + str(
                                index) + "\n"
                            self.instr += 1
                            self.llvm += "store float " + str(value) + ", float* %" + str(self.instr - 1) + ", align 4\n"
                        elif "char" in ltype:
                            llvmtype = ltype.replace("char", "i8")
                            llvmtype = llvmtype.replace("[]", "")
                            self.llvm += "%" + str(self.instr) + " = getelementptr inbounds [" + str(
                                size) + " x " + llvmtype + "], [" + str(size) + " x " + llvmtype + "]* %" + register + ", i64 0, i64 " + str(
                                index) + "\n"
                            self.instr += 1
                            self.llvm += "store i8 " + str(value) + ", i8* %" + str(self.instr - 1) + ", align 4\n"'''
                        #print("test")
                else:
                    if ltype == "int":
                        '''
                        if value[1] == "float":
                            self.llvm += "%" + str(self.instr) + " = fptosi float " + str(value[0]) + " to i32\n"
                            self.instr += 1
                        self.llvm += "store i32 %" + str(self.instr-1) + ", i32* " + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                        '''
                        print(value)
                        print("reg")
                        print(reg[0])
                        # self.llvm += "store i32 " + str(value) + ", i32* " + str(self.currentTable.lookup(currentNode.lvalue.var).register) + ", align 4\n"
                        context = self.FCStack.peek()
                        self.llvm += "sw " + value[0] + ", " + str(reg[0]) + "($sp) \n"
                        self.FCStack.removeTempReg(value[0])
                    elif ltype == "float":
                        if value[1] == "int":
                            self.llvm += "%" + str(self.instr) + " = sitofp i32 " + str(reg[0]) + " to float\n"
                            self.instr += 1
                        context = self.FCStack.peek()
                        self.llvm += "swc1 " + value[0] + ", " + str(reg[0]) + "($sp) \n"
                        self.FCStack.removeTempReg(value[0])
                        #self.llvm += "store float %" + str(self.instr-1) + ", float* " + self.currentTable.lookup(currentNode.lvalue.var).register + ", align 4\n"
                    elif ltype == "char":
                        context = self.FCStack.peek()
                        self.llvm += "sw " + value[0] + ", " + str(reg[0]) + "($sp) \n"
                        self.FCStack.removeTempReg(value[0])
                    if ltype == "int[]":
                        llvmtype = ltype.replace("int", "i32")
                        llvmtype = llvmtype.replace("[]", "")
                        try:
                            value = int(value[0])
                        except ValueError:
                            value = float(value[0])
                        self.llvm += "store i32 " + str(value) + ", i32* %" + str(self.instr - 1) + ", align 4\n"
                    elif ltype == "float[]":
                        llvmtype = ltype.replace("float", "float")
                        llvmtype = llvmtype.replace("[]", "")
                        try:
                            value = float(value[0])
                        except ValueError:
                            print("failiure")
                        packed = struct.pack("f", value)
                        value = struct.unpack("f", packed)[0]
                        self.llvm += "store float " + str(value) + ", float* %" + str(self.instr - 1) + ", align 4\n"
                    elif ltype == "char[]":
                        llvmtype = ltype.replace("char", "i8")
                        llvmtype = llvmtype.replace("[]", "")
                        self.llvm += "store i8 " + str(value) + ", i8* %" + str(self.instr - 1) + ", align 4\n"

            else:
                # In this case the lvalue is a pointer dereference
                value = currentNode.rvalue.accept(self)
                self.lvalue = True
                reg = currentNode.lvalue.accept(self)
                var = reg[3]
                type = reg[1]
                #print(value)
                #print(reg)
                print("Zen we hier mss?")
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
                        packed = struct.pack("f", value)
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

    def VisitString(self, currentNode):
        #print("SLComment")
        string = currentNode.value
        noquotes = string.encode('utf-8').decode('unicode-escape')
        formatchr = [c for c in noquotes]
        for chr in formatchr:
            if "\n" in chr:
                #print("JA?")
                formatchr[formatchr.index(chr)] = '\\' + hex(ord(chr)).replace("x", "")
        newformat = ""
        for c in formatchr:
            newformat += c
        #print(newformat)

        if newformat in self.printstr:
            size = len(newformat)
            #print(size)
            #print("string exists")
            for string in self.printstr:
                if string == newformat:
                    strindex = self.printstr.index(string)
            return ("@.str." + str(strindex), "string", str(size-1), "value")
        else:
            #print("The string has size:")
            #print(newformat)
            size = len(newformat)
            #print(size)
            strindex = len(self.printstr)
            string = "@.str." + str(strindex) + " = private unnamed_addr constant [" + str(size - 1) + " x i8] c\"" + str(newformat.replace("\"","")) + "\\00" + "\", align 1\n"
            #print(string)
            self.llvm = string + self.llvm
            self.printstr.append(format)
            return ("@.str." + str(strindex), "string", str(size-1), "value")

        return currentNode

    def VisitScanf(self, currentNode):
        #print("Scanf")
        format = currentNode.format.value
        #print(format)
        #print(len(format))

        params = []
        if not self.scanning:
            self.llvm = "declare i32 @__isoc99_scanf(i8* noundef, ...)\n" + self.llvm

        # Prepare arguments
        if currentNode.args:
            for child in currentNode.args.children:
                #print(child)
                self.lvalue = False
                node = child.accept(self)
                self.lvalue = True
                #print(node)
                # When the arg is reference and no value
                if isinstance(child, UnaryOperation):
                    node = (node[0], node[1], node[2], node[3], "ref")
                    params.append(node)
                # When the arg is a value
                elif node[2] == "reg":
                    symbol = self.currentTable.lookup(node[3])
                    type = symbol.type
                    #print(type)
                    if type == "int":
                        self.llvm += "%" + str(self.instr) + " = load i32, i32* " + str(
                            symbol.register) + ", align 4\n"
                        self.instr += 1
                    if type == "float":
                        self.llvm += "%" + str(self.instr) + " = load float, float* " + str(
                            symbol.register) + ", align 4\n"
                        self.instr += 1
                    if type == "char":
                        self.llvm += "%" + str(self.instr) + " = load i8, i8* " + str(
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
                    #print(node)
                    params.append(node)

        if format in self.printstr:
            '''
            print("string exists")
            '''
        else:
            size = len(format)-1
            #print("The format has size:")
            #print(size)
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
        self.llvm += "([" + str(size) + " x i8], ["+ str(size) + " x i8]* @.str." + str(strindex) + ", i32 0, i32 0)"
        #print("Parameters:")
        i = 1
        numberParams = len(params)
        #print(numberParams)
        if params:
            self.llvm += ", "
        for node in params:
            #print(node)
            if node[2] == "reg" and node[4] == "value":
                if node[1] == "int":
                    self.llvm += "i32* noundef " + str(node[0])
                elif node[1] == "float":
                    self.llvm += "float* noundef " + str(node[0])
                else:
                    self.llvm += "i8 noundef " + str(node[0])
            elif node[2] == "reg" and node[4] == "ref":
                if "[]" in node[1]:
                    symbol = self.currentTable.lookupUnallocated(node[3])
                    if node[1] == "int[]":
                        self.llvm += "[" + symbol.size + " x i32]*  noundef " + str(node[0])
                    elif node[1] == "float[]":
                        self.llvm += "[" + symbol.size + " x float]*  noundef " + str(node[0])
                    else:
                        self.llvm += "[" + symbol.size + " x i8]*  noundef " + str(node[0])
                else:
                    if "int" in node[1]:
                        self.llvm += "i32* noundef " + str(node[0])
                    elif "float" in node[1]:
                        self.llvm += "float* noundef " + str(node[0])
                    else:
                        self.llvm += "i8* noundef " + str(node[0])
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
        #print("Printf")
        format = currentNode.format.value
        #print(format)
        #print(str(format))
        #noquotes = format.replace("\"","")
        #noquotes = format.replace(r'\n', '\n')
        noquotes = format.encode('utf-8').decode('unicode-escape')
        #print(noquotes)
        formatchr = [c for c in noquotes]
        #print(formatchr)
        for chr in formatchr:
            if "\n" in chr:
                #print("JA?")
                formatchr[formatchr.index(chr)] = '\\' + hex(ord(chr)).replace("x", "")
        size = len(formatchr)
        #print(formatchr)
        newformat = ""
        for c in formatchr:
            newformat += c
        #print(newformat)
        params = []
        if not self.printing:
            self.llvm = "declare i32 @printf(i8* noundef, ...)\n" + self.llvm

        # Prepare arguments
        #print("prepare args")
        #print(currentNode.children)
        if currentNode.args:
            for child in currentNode.args:
                #print(child)
                if isinstance(child, ArrayVariable):
                    child.rvalue = True
                self.lvalue = False
                node = child.accept(self)
                self.lvalue = True
                #print(node)
                # When the arg is reference and no value
                if isinstance(child, UnaryOperation) and child.value == "*":
                    node = (node[0], node[1], node[2], node[3], "ref")
                    params.append(node)
                elif node[1] == "string":
                    params.append(node)
                # When the arg is a value
                elif node[2] == "reg":
                    symbol = self.currentTable.lookup(node[3].replace("()",""))
                    if "float" in node[1]:
                        self.llvm += "%" + str(self.instr) + " = fpext float " + str(node[0]) + " to double\n"
                        self.instr += 1
                    if isinstance(child, Variable) and "[]" in node[1]:
                        newnode = ("%"+ str(self.instr - 1), node[1], node[2], node[3], "array")
                    else:
                        newnode = ("%"+ str(self.instr - 1), node[1], node[2], node[3], "value")
                    params.append(newnode)
                else:
                    if "float" in node[1]:
                        self.llvm += "%" + str(self.instr) + " = fpext float " + str(node[0]) + " to double\n"
                        self.instr += 1
                    #print(node)
                    params.append(node)

        #print(self.printstr)
        if newformat in self.printstr:
            #print("string exists")
            for string in self.printstr:
                if string == newformat:
                    strindex = self.printstr.index(string)
        else:
            #print("The format has size:")
            #print(size)
            #print(newformat)
            strindex = len(self.printstr)
            '''
            packed = struct.pack("18c", format)
            print(packed)
            unpacked = struct.unpack("c", packed)[0]
            print(unpacked)
            '''
            string = "@.str." + str(strindex) + " = private unnamed_addr constant [" + str(size + 1) + " x i8] c\"" + str(newformat.replace("\"","")) + "\\00" + "\", align 1\n"
            #print(string)
            self.llvm = string + self.llvm
            self.printstr.append(format)

        # Print function call
        self.llvm += "%" + str(self.instr) + " = call i32 (i8*, ...)" + " @printf(i8* noundef getelementptr inbounds "
        self.llvm += "([" + str(size + 1) + " x i8], ["+ str(size + 1) + " x i8]* @.str." + str(strindex) + ", i32 0, i32 0)"
        #print("Parameters:")
        i = 1
        numberParams = len(params)
        #print(numberParams)
        if params:
            self.llvm += ", "
        for node in params:
            #print(node)
            if node[1] == "string":
                self.llvm += "i8* noundef getelementptr inbounds ([" + node[2] + " x i8], [" + node[2] + " x i8]* " + node[0] + ", i64 0, i64 0)"
            elif len(node) > 3 and node[4] == "array":
                #print("JAAAAAAAA")
                if node[1] == "int" or node[1] == "int[]":
                    self.llvm += "i32* noundef " + str(node[0])
                elif node[1] == "float" or node[1] == "float[]":
                    self.llvm += "float* noundef " + str(node[0])
                elif node[1] == "char" or node[1] == "char[]":
                    self.llvm += "i8* noundef " + str(node[0])
            elif node[2] == "reg" and node[4] == "value":
                if node[1] == "int" or node[1] == "int[]":
                    self.llvm += "i32 noundef " + str(node[0])
                elif node[1] == "float" or node[1] == "float[]":
                    self.llvm += "double noundef " + str(node[0])
                elif node[1] == "char" or node[1] == "char[]":
                    self.llvm += "i8 noundef " + str(node[0])
            elif node[2] == "reg" and node[4] == "ref":
                if "int" in node[1]:
                    self.llvm += "i32 noundef " + str(node[0])
                elif "float" in node[1]:
                    self.llvm += "double noundef " + str(node[0])
                else:
                    self.llvm += "i8 noundef " + str(node[0])
            elif node[2] == "value":
                if node[1] == "int":
                    self.llvm += "i32 noundef " + str(node[0])
                elif node[1] == "float":
                    packed = struct.pack("f", node[0])
                    value = struct.unpack("f", packed)[0]
                    #print(value)
                    self.llvm += "double noundef " + str(value)
                else:
                    char = ord(node[0].replace("\"","").replace("\'",""))
                    self.llvm += "i8 noundef " + str(char)



            if i != numberParams:
                self.llvm += ", "
            i += 1
        self.llvm += ")"
        self.llvm += "\n"
        self.instr += 1
        self.printing = True
        return currentNode


