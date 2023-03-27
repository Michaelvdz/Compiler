from AST import *
import graphviz

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class ASTVisitor(Visitor):

    def __init__(self):
        print("----------------Printing AST TREE----------------")
        self.ast = graphviz.Digraph('AST', filename='ast.gv')

    def VisitASTNode(self, currentNode):
        print("Beginning Node")
        self.ast.node(str(id(currentNode)), currentNode.name)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        print("Ending Node")
        return currentNode

    def VisitBinaryOperation(self, currentNode):
        print("Beginning Binary")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        print("Ending Binary")
        return currentNode

    def VisitUnaryOperation(self, currentNode):
        print("Beginning Unary")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        print("Ending Unary")
        return currentNode

    def VisitRelationOperation(self, currentNode):
        print("BeginningRelation")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        print("Endng Relation")
        return currentNode

    def VisitLogicalOperation(self, currentNode):
        print("Beginning Logical")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        print("Ending Logical")
        return currentNode

    def VisitConstant(self, currentNode):
        print("Beginning Constant")
        self.ast.node(str(id(currentNode)), currentNode.value)
        print("Ending Constant")
        return currentNode

    def VisitDeclaration(self, currentNode):
        print("Beginning Declaration")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        print("Ending Declaration")
        return currentNode

    def VisitAssignment(self, currentNode):
        print("Beginning Assignment")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)

            self.ast.edge(str(id(currentNode)), str(id(node)))
        print("Ending Assignment")
        return currentNode


