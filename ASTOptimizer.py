import copy

from AST import *
import graphviz

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class ASTOptimizer(Visitor):

    def __init__(self, tree):
        #self.ast = graphviz.Digraph('AST', filename='ast.gv')
        self.tree = tree

    def VisitASTNode(self, currentNode):
        print("Node")
        newNode = ASTNode(currentNode.name)
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode

    def VisitBinaryOperation(self, currentNode):
        print("Binary")
        children = []
        for child in currentNode.children:
            children.append(child.accept(self))

        match currentNode.value:
            case "+":
                print("We do +")
                value = 0
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    for child in children:
                        node = child.accept(self)
                        try:
                            int(node.value)
                            value += int(node.value)
                        except ValueError:
                            value += float(node.value)
                    currentNode.children = 0
                    currentNode.value = value
                    newnode = Constant(str(value))
                    print("WHOOOOOOOOOOOOOOOOOOOO")
                    return newnode
                else:
                    newnode = BinaryOperation(currentNode.value)
                    for child in children:
                        newnode.adopt(child)
                    return newnode
            case "*":
                value = 1
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    for child in children:
                        node = child.accept(self)
                        try:
                            int(node.value)
                            value *= int(node.value)
                        except ValueError:
                            value *= float(node.value)
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
                value = "NaN"
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    for child in children:
                        node = child.accept(self)
                        print("Recieved node with type: " + str(type(node)))
                        try:
                            int(node.value)
                            if value == "NaN":
                                print("Dit?")
                                value = int(node.value)
                            else:
                                print("Daarna dit?")
                                value = value / int(node.value)
                        except ValueError:
                            if value == "NaN":
                                value = float(node.value)
                            else:
                                value = value / float(node.value)
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
                value = 0
                if isinstance(children[0], Constant) and isinstance(children[1], Constant):
                    for child in children:
                        node = child.accept(self)
                        try:
                            int(node.value)
                            value -= int(node.value)
                        except ValueError:
                            value -= float(node.value)
                    currentNode.children = 0
                    currentNode.value = value
                    newnode = Constant(str(value))
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
        print("Binary")
        match currentNode.value:
            case "-":
                value = 0
                for child in currentNode.children:
                    node = child.accept(self)
                    try:
                        int("-"+node.value)
                        value = int("-"+node.value)
                    except ValueError:
                        value = float("-"+node.value)
                currentNode.children = 0
                currentNode.value = value
                node = Constant(str(value))
                return node
            case "!":
                for child in currentNode.children:
                    node = child.accept(self)
                    if node.value == "0" or node.value is False:
                        value = "true"
                    else:
                        value = "false"
                currentNode.children = 0
                currentNode.value = value
                node = Constant(str(value))
                return node
            case "_":
                print("none")
        return currentNode

    def VisitRelationOperation(self, currentNode):
        print("Relation")
        newNode = copy.copy(currentNode)
        newNode.children = []
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode

    def VisitLogicalOperation(self, currentNode):
        print("Logical")
        newNode = copy.copy(currentNode)
        newNode.children = []
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode

    def VisitConstant(self, currentNode):
        print("Constant")
        return currentNode

    def VisitDeclaration(self, currentNode):
        print("Declaration")
        newNode = copy.copy(currentNode)
        newNode.children = []

        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode

    def VisitAssignment(self, currentNode):
        print("Assignment")
        newNode = copy.copy(currentNode)
        newNode.children = []
        newNode.lvalue = currentNode.lvalue.accept(self)
        newNode.rvalue = currentNode.rvalue.accept(self)
        newNode.adopt(newNode.lvalue)
        newNode.adopt(newNode.rvalue)
        """
        for child in currentNode.children:
            node = child.accept(self)
            print(node)
            newNode.children.append(node)
        """
        return newNode


