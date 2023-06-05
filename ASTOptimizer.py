import copy

from colorama import Fore

from AST import *
import graphviz

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class ASTOptimizer(Visitor):

    vars = dict()
    propagation = True
    returnType = ""
    lvalue = False
    deref = False

    def __init__(self, tree):
        #self.ast = graphviz.Digraph('AST', filename='ast.gv')
        #print("---------------------Optimizing Tree--------------------")
        self.tree = tree
        self.lineNr = 0
        self.vars = dict()

    def VisitASTNode(self, currentNode, constantProp=True):
        #print("Node")


        if currentNode.name == "Inst":
            self.lineNr += 1
        newNode = ASTNode(currentNode.name)
        if not currentNode.children:
            #print("DOETEM DEES?")
            if self.propagation:
                if constantProp:
                    var = self.vars.get(currentNode.value)
                    if var:
                        #print("Var exist, lets do constant propagation")
                        newNode = Constant(var)
                    else:
                        newNode = Variable(currentNode.name)


        else:
            for child in currentNode.children:
                node = child.accept(self)
                newNode.children.append(node)
        return newNode

    def VisitInclude(self, currentNode):
        return currentNode

    def VisitBinaryOperation(self, currentNode):
        #print("Binary Optimisation")
        children = []
        for child in currentNode.children:
            children.append(child.accept(self))

        #print(children)
        #print(children[0].value)
        #print(children[1].value)


        match currentNode.value:
            case "+":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    #print("TYPEZ")
                    #print(children[0].type)
                    #print(children[1].type)
                    if (children[0].type == "int" or children[0].type == "float") and (children[1].type == "int" or children[1].type == "float"):
                        try:
                            value = int(children[0].value)
                            #print(int(children[0].value))
                        except ValueError:
                            value = float(children[0].value)

                        try:
                            value += int(children[1].value)
                            #print(int(children[1].value))
                        except ValueError:
                            value += float(children[1].value)

                        currentNode.children = 0
                        currentNode.value = value
                        newnode = Constant(str(value))
                        if (children[0].type == "float") or (children[1].type == "float"):
                            newnode.type = "float"
                        else:
                            newnode.type = "int"

                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode

            case "*":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    #print(children[0].type)
                    #print(children[1].type)
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        #print("GRAAKTEM IER?")
                        try:
                            value = int(children[0].value)
                        except ValueError:
                            value = float(children[0].value)

                        try:
                            value *= int(children[1].value)
                        except ValueError:
                            value *= float(children[1].value)

                        currentNode.children = 0
                        currentNode.value = value
                        newnode = Constant(str(value))
                        #print("We fold")
                        #print(value)
                        if (children[0].type == "float") or (children[1].type == "float"):
                            newnode.type = "float"
                        else:
                            newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "/":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        try:
                            value = int(children[0].value)
                        except ValueError:
                            value = float(children[0].value)

                        if isinstance(value, float):
                                value = value / float(children[1].value)
                        else:
                            try:
                                try:
                                    value = value // int(children[1].value)
                                except ValueError:
                                    value = value / float(children[1].value)
                            except ZeroDivisionError:
                                print(
                                    "\n" + Fore.MAGENTA + "[warning] " + Fore.RESET + "line " + str(
                                        self.lineNr) + ": Division by zero is undefined \n")
                                currentNode.children = 0
                                currentNode.value = value
                                newnode = Constant("NaN")
                                return newnode
                        currentNode.children = 0
                        currentNode.value = value
                        newnode = Constant(str(value))
                        if (children[0].type == "float") or (children[1].type == "float"):
                            newnode.type = "float"
                        else:
                            newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "%":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        try:
                            value = int(children[0].value)
                        except ValueError:
                            value = float(children[0].value)

                        try:
                            try:
                                value = value % int(children[1].value)
                            except ValueError:
                                value = value % float(children[1].value)
                        except ZeroDivisionError:
                            print(
                                "\n" + Fore.MAGENTA + "[warning] " + Fore.RESET + "line " + str(
                                    self.lineNr) + ": Division by zero is undefined \n")
                            currentNode.children = 0
                            currentNode.value = value
                            newnode = Constant("NaN")
                            return newnode
                        currentNode.children = 0
                        currentNode.value = value
                        newnode = Constant(str(value))
                        if (children[0].type == "float") or (children[1].type == "float"):
                            newnode.type = "float"
                        else:
                            newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "-":
                #print(children[0].varType)
                #print(children[1].varType)
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        try:
                            value = int(children[0].value)
                        except ValueError:
                            value = float(children[0].value)

                        try:
                            value -= int(children[1].value)
                        except ValueError:
                            value -= float(children[1].value)

                        currentNode.children = 0
                        currentNode.value = value
                        newnode = Constant(str(value))
                        if (children[0].type == "float") or (children[1].type == "float"):
                            newnode.type = "float"
                        else:
                            newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case ">":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        value1 = children[0].value
                        value2 = children[1].value
                        try:
                            value1 = int(value1)
                        except ValueError:
                            value1 = float(value1)
                        try:
                            value2 = int(value2)
                        except ValueError:
                            value2 = float(value2)

                        if value1 > value2:
                            newvalue = "1"
                        else:
                            newvalue = "0"
                        newnode = Constant(newvalue)
                        newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "<":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        value1 = children[0].value
                        value2 = children[1].value
                        try:
                            value1 = int(value1)
                        except ValueError:
                            value1 = float(value1)
                        try:
                            value2 = int(value2)
                        except ValueError:
                            value2 = float(value2)

                        if value1 < value2:
                            newvalue = "1"
                        else:
                            newvalue = "0"
                        newnode = Constant(newvalue)
                        newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "==":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        value1 = children[0].value
                        value2 = children[1].value
                        try:
                            value1 = int(value1)
                        except ValueError:
                            value1 = float(value1)
                        try:
                            value2 = int(value2)
                        except ValueError:
                            value2 = float(value2)

                        if value1 == value2:
                            newvalue = "1"
                        else:
                            newvalue = "0"
                        newnode = Constant(newvalue)
                        newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "!=":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        value1 = children[0].value
                        value2 = children[1].value
                        try:
                            value1 = int(value1)
                        except ValueError:
                            value1 = float(value1)
                        try:
                            value2 = int(value2)
                        except ValueError:
                            value2 = float(value2)

                        if value1 != value2:
                            newvalue = "1"
                        else:
                            newvalue = "0"
                        newnode = Constant(newvalue)
                        newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case ">=":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        value1 = children[0].value
                        value2 = children[1].value
                        try:
                            value1 = int(value1)
                        except ValueError:
                            value1 = float(value1)
                        try:
                            value2 = int(value2)
                        except ValueError:
                            value2 = float(value2)

                        if value1 >= value2:
                            newvalue = "1"
                        else:
                            newvalue = "0"
                        newnode = Constant(newvalue)
                        newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "<=":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        value1 = children[0].value
                        value2 = children[1].value
                        try:
                            value1 = int(value1)
                        except ValueError:
                            value1 = float(value1)
                        try:
                            value2 = int(value2)
                        except ValueError:
                            value2 = float(value2)

                        if value1 <= value2:
                            newvalue = "1"
                        else:
                            newvalue = "0"
                        newnode = Constant(newvalue)
                        newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "&&":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        value1 = children[0].value
                        value2 = children[1].value
                        try:
                            value1 = int(value1)
                        except ValueError:
                            value1 = float(value1)
                        try:
                            value2 = int(value2)
                        except ValueError:
                            value2 = float(value2)

                        if abs(value1) > 0:
                            value1 = 1
                        else:
                            value1 = 0
                        if abs(value2) > 0:
                            value2 = 1
                        else:
                            value2 = 0
                        if value1 and value2:
                            newvalue = "1"
                        else:
                            newvalue = "0"
                        newnode = Constant(newvalue)
                        newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "||":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    if (children[0].type == "int" or children[0].type == "float") and (
                            children[1].type == "int" or children[1].type == "float"):
                        value1 = children[0].value
                        value2 = children[1].value
                        try:
                            value1 = int(value1)
                        except ValueError:
                            value1 = float(value1)
                        try:
                            value2 = int(value2)
                        except ValueError:
                            value2 = float(value2)

                        if abs(value1) > 0:
                            value1 = 1
                        else:
                            value1 = 0
                        if abs(value2) > 0:
                            value2 = 1
                        else:
                            value2 = 0
                        if value1 or value2:
                            newvalue = "1"
                        else:
                            newvalue = "0"
                        newnode = Constant(newvalue)
                        newnode.type = "int"
                        return newnode
                    else:
                        newnode = BinaryOperation(currentNode.value)
                        newnode.line = currentNode.line
                        newnode.column = currentNode.column
                        for child in children:
                            newnode.adopt(child)
                        return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    newnode.line = currentNode.line
                    newnode.column = currentNode.column
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "_":
                print("none")
        return currentNode



    def VisitUnaryOperation(self, currentNode):
        #print("Unary")
        #print(currentNode.value)
        children = []

        match currentNode.value:
            case "-":
                #print("Tis -, kijken naar kinderen")
                value = 0
                node = currentNode.children[0].accept(self)
                if isinstance(node, Constant):
                    try:
                        value = -int(node.value)
                    except ValueError:
                        value = -float(node.value)
                    currentNode.children = 0
                    currentNode.value = value
                    node = Constant(str(value))
                    if isinstance(value, int):
                        node.type = "int"
                    else:
                        node.type = "float"
                    return node
                else:
                    #print("Tis -, als genne constante is, gwn node terugegeven")
                    node = currentNode.children[0].accept(self)
                    if isinstance(node, Constant):
                        try:
                            value = -int(node.value)
                        except ValueError:
                            value = -float(node.value)
                        currentNode.children = 0
                        currentNode.value = value
                        node = Constant(str(value))
                        if isinstance(value, int):
                            node.type = "int"
                        else:
                            node.type = "float"
                        return node
                    else:
                        currentNode.children = 0
                        currentNode.children = []
                        currentNode.children.append(node)
                    return currentNode
            case "--":
                '''
                if isinstance(currentNode.children[0], Constant):
                    for child in currentNode.children:
                        node = child.accept(self)
                        try:
                            value = int(node.value) - 1
                        except ValueError:
                            value = float(node.value) - 1
                    currentNode.children = 0
                    currentNode.value = value
                    node = Constant(str(value))
                    return node
                else:
                '''
                return currentNode
            case "+":
                #print("Tis +, kijken naar kinderen")
                value = 0
                node = currentNode.children[0].accept(self)
                if isinstance(node, Constant):
                    try:
                        value = int(node.value)
                    except ValueError:
                        value = float(node.value)
                    currentNode.children = 0
                    currentNode.value = value
                    node = Constant(str(value))
                    if isinstance(value, int):
                        node.type = "int"
                    else:
                        node.type = "float"
                    return node
                else:
                    #print("Tis +, gewoon kund teruggeven")
                    return node
            case "++":
                '''
                if isinstance(currentNode.children[0], Constant):
                    for child in currentNode.children:
                        node = child.accept(self)
                        try:
                            value = int(node.value) + 1
                        except ValueError:
                            value = float(node.value) + 1
                    currentNode.children = 0
                    currentNode.value = value
                    node = Constant(str(value))
                    return node
                else:
                '''
                return currentNode
            case "!":
                #print(currentNode.children[0].value)
                node = currentNode.children[0].accept(self)
                if isinstance(node, Constant):
                    for child in currentNode.children:
                        node = child.accept(self)
                        try:
                            value = int(node.value)
                        except ValueError:
                            value = float(node.value)
                        if abs(value) > 0:
                            value = 1
                        else:
                            value = 0
                        if value == 1:
                            newvalue = "0"
                        else:
                            newvalue = "1"
                    currentNode.children = 0
                    currentNode.value = newvalue
                    node = Constant(newvalue)
                    return node
                else:
                    currentNode.children = 0
                    currentNode.children = []
                    currentNode.children.append(node)
                    return currentNode
            case "[]":
                if isinstance(currentNode.children[0], Constant) or isinstance(currentNode.children[0], BinaryOperation):
                    for child in currentNode.children:
                        node = child.accept(self)
                        if isinstance(node, ASTNode):
                            try:
                                value = int(node.value)
                            except ValueError:
                                print("failure")
                    array = Array('[]')
                    array.size = value
                    #print(value)
                    currentNode.children = []
                    currentNode.adopt(array)
                    return currentNode
                else:
                    return currentNode
            case "_":
                print("none")
        return currentNode

    def VisitRelationOperation(self, currentNode):
        #print("Relation")
        newNode = copy.copy(currentNode)
        newNode.children = []
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode

    def VisitPointer(self, currentNode):
        #print("Pointer")
        if self.deref:
            print("Deref")
            newNode = UnaryOperation("*")
            for child in currentNode.children:
                node = child.accept(self)
                newNode.children.append(node)
            return newNode
        else:
            newNode = copy.copy(currentNode)
            newNode.children = []
            for child in currentNode.children:
                node = child.accept(self)
                newNode.children.append(node)
            return newNode

    def VisitArrayVariable(self, currentNode):
        #print("Pointer")
        newNode = copy.copy(currentNode)
        newNode.children = []
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode

    def VisitArray(self, currentNode):
        #print("Array")
        newNode = copy.copy(currentNode)
        size = currentNode.size.accept(self)
        #print(size.value)
        newNode.value = "[" + " ]"
        newNode.name = newNode.value
        newNode.children = []
        newNode.size = size
        #print(size)
        return newNode

    def VisitLogicalOperation(self, currentNode):
        #print("Logical")
        newNode = copy.copy(currentNode)
        newNode.children = []
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode

    def VisitFunction(self, currentNode):
        #print("Function in Opti")
        newNode = copy.copy(currentNode)
        #print(newNode.params)
        newNode.children.clear();
        self.returnType = currentNode.returnType.value
        if currentNode.hasbody:
            if currentNode.body:
                newNode.body = currentNode.body.accept(self)
                for child in newNode.body.children:
                    #print("Child")
                    if isinstance(child, Jump):
                        child.type = currentNode.returnType.value
                    newNode.children.append(child)
                    '''
                    print("test")
                    node = child.accept(self)
                    print(node)
                    if isinstance(node, Jump):
                        print("Jumper")
                        print(node.value)
                        if node.value == "return":
                            print("value:")
                            print(currentNode.returnType.value)
                            node.type = currentNode.returnType.value
                    newNode.children.append(node)
                    '''
        return newNode

    def VisitConstant(self, currentNode):
        #print("Constant")
        value = currentNode.value
        #print(currentNode.varType)
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                value = value
        #print(value)
        if isinstance(value, int):
            #print("Int?")
            if value > 2147483647 or value < -2147483648:
                #print("Dees kan ni")
                if value > 2147483647:
                    while(value > 2147483647):
                        value -= 2147483647
                elif value < -2147483648:
                    while(value > 2147483647):
                        value += 2147483647
                currentNode.value = value
            currentNode.type = "int"
            return currentNode
        elif isinstance(value, float):
            currentNode.type = "float"
            return currentNode
        else:
            currentNode.type = "char"
            return currentNode
        return currentNode

    def VisitVariable(self, currentNode):
        #print("Constant")
        if currentNode.children:
            for child in currentNode.children:
                if isinstance(child, Array):
                    currentNode.size = str(child.size.value)
        if currentNode.value in self.vars:
            #print(self.lvalue)
            if not self.lvalue:
                #print("Ja")
                return self.vars.get(currentNode.value)
            else:
                '''
                #print("Nee")
                '''
        return currentNode

    def VisitJump(self, currentNode):
        #print("---------------------------------------Jump")
        if currentNode.value == "return":
            currentNode.type =self.returnType
        return currentNode

    def VisitWhile(self, currentNode):
        #print("Loop")
        newNode = copy.copy(currentNode)
        #newNode.children.append(currentNode.body)
        '''
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        '''
        return newNode
    def VisitConditional(self, currentNode):
        #print("Conditional")
        #newNode = Conditional(currentNode.value)
        newNode = copy.copy(currentNode)
        newNode.children = []
        #print(len(currentNode.children))
        #print(len(newNode.children))
        condition = currentNode.condition.accept(self)
        neverTrue = False
        if isinstance(condition, Constant):
            if condition.value == "0":
                neverTrue = True
        newNode.condition = condition

        ifbody = currentNode.ifbody.accept(self)
        print(ifbody)
        newNode.ifbody = ifbody
        if currentNode.elsebody:
            elsebody = currentNode.elsebody.accept(self)
            newNode.elsebody = elsebody
            if neverTrue:
                return elsebody
        if neverTrue:
            return False

        return newNode

    def VisitExprLoop(self, currentNode):
        #print("LoopExpr")
        newNode = ExprLoop(currentNode.value)
        newNode.children = []
        for child in currentNode.children:
            node = child.accept(self)
            print(node)
            #print("Recieved node")
            #print(node.children)
            if node is not False:
                newNode.children.append(node)
            if isinstance(node, Jump):
                if node.value == "return":
                    #print("We zen hier")
                    #print(newNode)
                    return newNode
                if node.value == "break":
                    return newNode
                if node.value == "continue":
                    return newNode
        return newNode

    def VisitScope(self, currentNode):
        #print("Scope")
        newNode = copy.copy(currentNode)
        newNode.children = []
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
            if isinstance(node, Jump):
                if node.value == "return":
                    return newNode
                if node.value == "break":
                    return newNode
                if node.value == "continue":
                    return newNode
        return newNode

    def VisitDeclaration(self, currentNode):
        #print("Declaration")
        newNode = copy.copy(currentNode)
        newNode.children = []
        for child in currentNode.children:
            if not isinstance(child, Array):
                node = child.acceptWithNoOptimization(self)
                newNode.children.append(node)
            else:
                newNode.type += "[]"
                node = child.accept(self)
                newNode.children.append(node)
        return newNode

    def VisitCall(self, currentNode):
        #print("VisitCall")
        newNode = copy.copy(currentNode)
        newNode.children = []
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode

    def VisitAssignment(self, currentNode):
        #print("Assignment")
        newNode = copy.copy(currentNode)
        newNode.children = []
        #print(currentNode.lvalue)
        self.lvalue = True
        if not isinstance(currentNode.lvalue, Declaration):
            self.deref = True
        newNode.lvalue = currentNode.lvalue.accept(self)
        self.deref = False
        self.lvalue = False
        #print(newNode.lvalue)
        if isinstance(newNode.lvalue, Array):
            '''
            print("ARAAAAAAAAAAAAAAAAAAAAAAAAY")
            print(newNode.lvalue.size)
            '''
        #print(newNode.lvalue)
        newNode.rvalue = currentNode.rvalue.accept(self)
        newNode.adopt(newNode.lvalue)
        newNode.adopt(newNode.rvalue)

        if isinstance(newNode.lvalue, Declaration):
            if newNode.lvalue.attr == "const":
                #print("Ja?????")
                if isinstance(newNode.rvalue, Constant):
                    #print("Adding to the dict")
                    const = Constant(newNode.rvalue)
                    self.vars[newNode.lvalue.var] = const.value
        #print(self.vars)
        #print("Wa is dees na?")
        #newNode.rvalue.print()


        return newNode

    def VisitPointerDeref(self, currentNode):
        last = self.getLastStar(currentNode.children[0])
        last.adopt(currentNode.variable)
        return currentNode.children[0]

    def getLastStar(self, star):
        if star.children:
            return self.getLastStar(star.children[0])
        else:
            return star

    def VisitMLComment(self, currentNode):
        #print("MLComment")
        return currentNode

    def VisitSLComment(self, currentNode):
        #print("SLComment")
        return currentNode

    def VisitString(self, currentNode):
        #print("SLComment")
        return currentNode

    def VisitPrintf(self, currentNode):
        #print("DOETEM DEES FEITELIJK?????")
        #print("PrintF")
        #print(self.vars)
        newNode = PrintF(currentNode.value)
        newNode.line = currentNode.line
        newNode.column = currentNode.column
        newNode.children = []
        newNode.args = []
        node = None
        format = currentNode.format
        newNode.format = format
        #print(len(currentNode.children))
        for child in currentNode.args:
            node = child.accept(self)
            #print("optimized node")
            #print(node)
            newNode.children.append(node)
            newNode.args.append(node)
        #node = currentNode.args.accept(self)
        #newNode.args.append(node)
        #print(newNode.format)
        #print(newNode.children)
        return newNode

    def VisitScanf(self, currentNode):
        #print("PrintF")
        newNode = copy.copy(currentNode)
        newNode.children = []
        self.propagation = False
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        self.propagation = True
        return newNode

