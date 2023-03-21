import copy

from AST import *
import graphviz

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class ASTOptimizer(Visitor):

    def __init__(self, tree):
        self.ast = graphviz.Digraph('AST', filename='ast.gv')
        self.tree = tree

    def VisitASTNode(self, currentNode):
        print("Node")
        newNode = ASTNode(currentNode.name)
        for child in currentNode.children:
            node = child.accept(self)
            node.print()
            newNode.children.append(node)
        return newNode

    def VisitBinaryOperation(self, currentNode):
        print("Binary")
        match currentNode.value:
            case "+":
                value = 0
                for child in currentNode.children:
                    node = child.accept(self)
                    try:
                        int(node.value)
                        value += int(node.value)
                    except ValueError:
                        value += float(node.value)
            case "*":
                value = 1
                for child in currentNode.children:
                    node = child.accept(self)
                    try:
                        int(node.value)
                        value *= int(node.value)
                    except ValueError:
                        value *= float(node.value)
            case "/":
                value = "NaN"
                for child in currentNode.children:
                    node = child.accept(self)
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
            case "-":
                value = "NaN"
                for child in currentNode.children:
                    node = child.accept(self)
                    try:
                        int(node.value)
                        if value == "NaN":
                            value = int(node.value)
                        else:
                            value = value - int(node.value)
                    except ValueError:
                        if value == "NaN":
                            value = float(node.value)
                        else:
                            value = value - float(node.value)
            case "_":
                print("none")
        print(value)
        currentNode.children = 0
        currentNode.value = value
        node = Constant(str(value))
        return node

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
        print(type(currentNode))
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
        for child in currentNode.children:
            node = child.accept(self)
            newNode.children.append(node)
        return newNode


