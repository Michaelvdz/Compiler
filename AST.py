from ASTVisitor import Visitor


class ASTTree:

    name = ""
    root = 0

    def __init__(self, name=""):
        self.root = 0
        self.name = name

    def setRoot(self, node):
        self.root = node

    def print(self):
        self.root.print()


class ASTNode:

    def __init__(self, name="Free"):
        print("___init-ASTNode___");
        self.children = []
        self.name = name
        print("___Node-Created-With-Name:"+ self.name + "___")

    def print(self):
        if not self.children:
            print(self.name)
        else:
            print(self.name)
            print("With children")
            for node in self.children:
                node.print()

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            print("Adding node: " + node.name)
            self.children.append(node)

    def accept(self, visitor: Visitor):
        value = visitor.VisitASTNode(self)
        print(value)
        return value

class BinaryOperation(ASTNode):

    name = ""
    children = []
    operator = ""

    def __init__(self, name):
        print("___init-BinaryOperation___");
        self.children = []
        self.name = "BinaryOperation"
        self.operator = name
        print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a binary operation node with operator: " + str(self.operator) + " and nodes:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitBinaryOperation(self)


class Constant(ASTNode):

    name = ""
    children = []
    value = ""

    def __init__(self, value):
        print("___init-Constant__");
        self.children = 0
        self.name = "Constant"
        self.value = value
        print("___Node-Created-With-Name:"+ self.name + "___")

    def print(self):
        print("Constant: " + self.value)

    def accept(self, visitor: Visitor):
        return visitor.VisitConstant(self)





