from AST import *
import graphviz

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class ASTVisitor(Visitor):

    def __init__(self):
        self.ast = graphviz.Digraph('AST', filename='ast.gv')

    def VisitASTNode(self, currentNode):
        self.ast.node(currentNode.name)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(currentNode.name, str(node))
        return currentNode.name

    def VisitBinaryOperation(self, currentNode):
        self.ast.node(currentNode.operator)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(currentNode.operator, node)
        return currentNode.operator

    def VisitConstant(self, currentNode):
        self.ast.node(currentNode.value)
        return currentNode.value

