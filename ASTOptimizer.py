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

    def __init__(self, tree):
        #self.ast = graphviz.Digraph('AST', filename='ast.gv')
        #print("---------------------Optimizing Tree--------------------")
        self.tree = tree
        self.lineNr = 0

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

    def VisitBinaryOperation(self, currentNode):
        #print("Binary")
        children = []
        for child in currentNode.children:
            children.append(child.accept(self))

        print(children[0])
        match currentNode.value:
            case "+":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    try:
                        value = int(children[0].value)
                    except ValueError:
                        value = float(children[0].value)
                    try:
                        value += int(children[1].value)
                    except ValueError:
                        value += float(children[1].value)
                    currentNode.children = 0
                    currentNode.value = value
                    newnode = Constant(str(value))
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode

            case "*":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "/":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "%":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "-":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case ">":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "<":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "==":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "!=":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case ">=":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "<=":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "&&":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "||":
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
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
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "_":
                print("none")
        return currentNode



    def VisitUnaryOperation(self, currentNode):
        #print("Unary")
        match currentNode.value:
            case "-":
                value = 0
                for child in currentNode.children:
                    node = child.accept(self)
                    try:
                        value = -int(node.value)
                    except ValueError:
                        value = -float(node.value)
                currentNode.children = 0
                currentNode.value = value
                node = Constant(str(value))
                return node
            case "--":
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
            case "+":
                value = 0
                for child in currentNode.children:
                    node = child.accept(self)
                    try:
                        value = int(node.value)
                    except ValueError:
                        value = float(node.value)
                currentNode.children = 0
                currentNode.value = value
                node = Constant(str(value))
                return node
            case "++":
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
            case "!":
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

    def VisitLogicalOperation(self, currentNode):
        #print("Logical")
        newNode = copy.copy(currentNode)
        newNode.children = []
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode

    def VisitFunction(self, currentNode):
        #print("Function")
        newNode = copy.copy(currentNode)
        newNode.children = []
        newNode.body = currentNode.body.accept(self)
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode

    def VisitConstant(self, currentNode):
        #print("Constant")
        return currentNode

    def VisitVariable(self, currentNode):
        #print("Constant")
        return currentNode

    def VisitJump(self, currentNode):
        print("---------------------------------------Jump")
        return currentNode

    def VisitWhile(self, currentNode):
        print("Loop")
        newNode = copy.copy(currentNode)
        #newNode.children.append(currentNode.body)
        '''
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        '''
        return newNode
    def VisitConditional(self, currentNode):
        print("Conditional")
        newNode = copy.copy(currentNode)
        newNode.children = []
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode

    def VisitExprLoop(self, currentNode):
        print("LoopExpr")
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

    def VisitScope(self, currentNode):
        print("Scope")
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
        print("Declaration")
        newNode = copy.copy(currentNode)
        newNode.children = []
        for child in currentNode.children:
            node = child.acceptWithNoOptimization(self)
            newNode.children.append(node)
        return newNode

    def VisitAssignment(self, currentNode):
        #print("Assignment")
        newNode = copy.copy(currentNode)
        newNode.children = []
        #print(currentNode.lvalue)
        newNode.lvalue = currentNode.lvalue.accept(self)
        #print(newNode.lvalue)
        newNode.rvalue = currentNode.rvalue.accept(self)
        newNode.adopt(newNode.lvalue)
        newNode.adopt(newNode.rvalue)

        #print("Wa is dees na?")
        #newNode.rvalue.print()
        if not newNode.rvalue.children:
            #print('No kids')
            #print(newNode.lvalue)
            if isinstance(newNode.lvalue, Declaration):
                #print("Invoegen?")
                self.vars[newNode.lvalue.var] = newNode.rvalue.value
                for key, value in self.vars.items():
                    x = "test"
                    #print(key + ': ' + value)
            elif isinstance(newNode.lvalue, Variable):
                print("We are assigning a new value")
                if self.vars.get(newNode.lvalue.value):
                    self.vars.pop(newNode.lvalue.value)


        return newNode

    def VisitMLComment(self, currentNode):
        #print("MLComment")
        return currentNode

    def VisitSLComment(self, currentNode):
        #print("SLComment")
        return currentNode

    def VisitPrintf(self, currentNode):
        print("DOETEM DEES FEITELIJK?")
        #print("PrintF")
        newNode = copy.copy(currentNode)
        newNode.children = []
        self.propagation = False
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        self.propagation = True
        return newNode


