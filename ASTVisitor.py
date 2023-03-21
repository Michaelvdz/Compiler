from AST import *
import graphviz

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class ASTVisitor(Visitor):

    def __init__(self):
        self.ast = graphviz.Digraph('AST', filename='ast.gv')

    def VisitASTNode(self, currentNode):
        print("Node")
        print(id(currentNode))
        self.ast.node(str(id(currentNode)), currentNode.name)
        print(currentNode.name)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        return currentNode

    def VisitBinaryOperation(self, currentNode):
        print("Binary")
        print(id(currentNode))
        print(currentNode.print())
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        return currentNode

    def VisitUnaryOperation(self, currentNode):
        print("Unary")
        print(id(currentNode))
        print(currentNode.print())
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        return currentNode

    def VisitRelationOperation(self, currentNode):
        print("Relation")
        print(id(currentNode))
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        return currentNode

    def VisitLogicalOperation(self, currentNode):
        print("Logical")
        print(id(currentNode))
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        return currentNode

    def VisitConstant(self, currentNode):
        print("Constant")
        print(id(currentNode))
        self.ast.node(str(id(currentNode)), currentNode.value)
        return currentNode

    def VisitDeclaration(self, currentNode):
        print("Declaration")
        print(id(currentNode))
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        return currentNode

    def VisitAssignment(self, currentNode):
        print("Assignment")
        print(id(currentNode))
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        return currentNode


