from AST import *
import graphviz

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class ASTVisitor(Visitor):

    def __init__(self, filename="", path="."):
        #print("----------------Printing AST TREE----------------")
        self.ast = graphviz.Digraph('AST', filename=filename+'.dot', directory=path)

    def VisitASTNode(self, currentNode):
        #print("Beginning Node")
        self.ast.node(str(id(currentNode)), currentNode.name)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Node")
        return currentNode

    def VisitInclude(self, currentNode):
        #print("Beginning Node")
        self.ast.node(str(id(currentNode)), currentNode.name)
        return currentNode

    def VisitConditional(self, currentNode):
        #print("Beginning Node")
        self.ast.node(str(id(currentNode)), currentNode.name)
        condition = currentNode.condition.accept(self)
        self.ast.edge(str(id(currentNode)), str(id(condition)), "Condition")
        ifbody = currentNode.ifbody.accept(self)
        self.ast.edge(str(id(currentNode)), str(id(ifbody)), "If-body")
        if not currentNode.elsebody == 0:
            elsebody = currentNode.elsebody.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(elsebody)), "Else-body")
        #print("Ending Node")
        return currentNode

    def VisitWhile(self, currentNode):
        #print("Beginning Node")
        self.ast.node(str(id(currentNode)), currentNode.name)
        if currentNode.beforeLoop:
            beforeLoop = currentNode.beforeLoop.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(beforeLoop)), "Before Loop")
        condition = currentNode.condition.accept(self)
        self.ast.edge(str(id(currentNode)), str(id(condition)), "Condition")
        body = currentNode.body.accept(self)
        self.ast.edge(str(id(currentNode)), str(id(body)), "Body")
        if currentNode.afterLoop:
            afterLoop = currentNode.afterLoop.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(afterLoop)), "After Loop")
        #print("Ending Node")
        return currentNode

    def VisitFunction(self, currentNode):
        #print("Beginning Function")
        self.ast.node(str(id(currentNode)), currentNode.name+"()")
        ret = currentNode.returnType.accept(self)
        self.ast.edge(str(id(currentNode)), str(id(ret)), "Return Type")

        if currentNode.params:
            for child in currentNode.params:
                param = child.accept(self)
                self.ast.edge(str(id(currentNode)), str(id(param)), "Parameter")

        if currentNode.body:
            body = currentNode.body.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(body)), "Body")
        #print("Ending Function")
        return currentNode

    def VisitScope(self, currentNode):
        #print("Beginning Node")
        self.ast.node(str(id(currentNode)), currentNode.name)
        if currentNode.children and len(currentNode.children) != 0:
            for child in currentNode.children:
                if child is not None:
                    node = child.accept(self)
                    self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Node")
        return currentNode

    def VisitExprLoop(self, currentNode):
        #print("Beginning Node")
        self.ast.node(str(id(currentNode)), currentNode.name)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Node")
        return currentNode


    def VisitCall(self, currentNode):
        #print("Beginning Node")
        self.ast.node(str(id(currentNode)), currentNode.value)
        if currentNode.children:
            for child in currentNode.children:
                node = child.accept(self)
                self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Node")
        return currentNode

    def VisitBinaryOperation(self, currentNode):
        #print("Beginning Binary")
        #print(currentNode.value)
        #print(str(id(currentNode)))
        self.ast.node(str(id(currentNode)), str(currentNode.value))
        #print("test")
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Binary")
        return currentNode

    def VisitUnaryOperation(self, currentNode):
        #print("Beginning Unary")
        #print(currentNode.value)
        #print(currentNode)
        self.ast.node(str(id(currentNode)), str(currentNode.value))
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Unary")
        return currentNode

    def VisitRelationOperation(self, currentNode):
        #print("BeginningRelation")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Endng Relation")
        return currentNode

    def VisitLogicalOperation(self, currentNode):
        #print("Beginning Logical")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Logical")
        return currentNode

    def VisitConstant(self, currentNode):
        #print("Beginning Constant")
        #print(currentNode.value.replace("'",""))
        self.ast.node(str(id(currentNode)), str(currentNode.value.replace("'","")))
        #print("Ending Constant")
        return currentNode

    def VisitJump(self, currentNode):
        #print("Beginning Jump")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Jump")
        return currentNode


    def VisitVariable(self, currentNode):
        #print("Beginning Constant")
        if currentNode.attr == "[]":
            self.ast.node(str(id(currentNode)), (currentNode.value))
            if currentNode.type:
                self.ast.node(str(id(currentNode.type)), currentNode.type)
                self.ast.edge(str(id(currentNode)), str(id(currentNode.type)))
            if currentNode.attr:
                self.ast.node(str(id(currentNode.attr)), (currentNode.attr))
                self.ast.edge(str(id(currentNode)), str(id(currentNode.attr)))
            if currentNode.size:
                self.ast.node(str(id(currentNode.size)), (currentNode.size))
                self.ast.edge(str(id(currentNode)), str(id(currentNode.size)))

        else:
            self.ast.node(str(id(currentNode)), currentNode.value)
            if currentNode.type:
                self.ast.node(str(id(currentNode.type)), currentNode.type)
                self.ast.edge(str(id(currentNode)), str(id(currentNode.type)))
            if currentNode.attr:
                self.ast.node(str(id(currentNode.attr)), str(id(currentNode.type)))
                self.ast.edge(str(id(currentNode)), str(id(currentNode.attr)))

        #print("Ending Constant")
        return currentNode

    def VisitArrayVariable(self, currentNode):
        #print("Beginning ArrayVar")
        self.ast.node(str(id(currentNode)), (currentNode.value)+"[]")
        if currentNode.type:
            self.ast.node(str(id(currentNode.type)), currentNode.type)
            self.ast.edge(str(id(currentNode)), str(id(currentNode.type)))
        if currentNode.attr:
            self.ast.node(str(id(currentNode.attr)), (currentNode.attr))
            self.ast.edge(str(id(currentNode)), str(id(currentNode.attr)))
        if currentNode.size:
            self.ast.node(str(id(currentNode.size)), (currentNode.size))
            self.ast.edge(str(id(currentNode)), str(id(currentNode.size)))
        if currentNode.index:
            self.ast.node(str(id(currentNode.index)), str(currentNode.index.value))
            self.ast.edge(str(id(currentNode)), str(id(currentNode.index)), "index")
        #print("Ending Constant")
        return currentNode

    def VisitArray(self, currentNode):
        #print("Beginning Declaration")
        self.ast.node(str(id(currentNode)), currentNode.value)
        node = currentNode.size.accept(self)
        self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Declaration")
        return currentNode

    def VisitDeclaration(self, currentNode):
        #print("Beginning Declaration")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Declaration")
        return currentNode

    def VisitPointer(self, currentNode):
        #print("Beginning Declaration")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Declaration")
        return currentNode

    def VisitAssignment(self, currentNode):
        #print("Beginning Assignment")
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Assignment")
        return currentNode

    def VisitPointerDeref(self, currentNode):
        self.ast.node(str(id(currentNode)), currentNode.value)
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        #print("Ending Assignment")
        var = currentNode.variable.accept(self)
        self.ast.edge(str(id(currentNode)), str(id(var)))
        return currentNode
    def VisitMLComment(self, currentNode):
        #print("Beginning MLComment")
        self.ast.node(str(id(currentNode)), currentNode.value)
        #print("Ending Assignment")
        return currentNode

    def VisitSLComment(self, currentNode):
        #print("Beginning SLComment")
        self.ast.node(str(id(currentNode)), currentNode.value)
        #print("Ending Assignment")
        return currentNode

    def VisitString(self, currentNode):
        #print("Beginning SLComment")
        self.ast.node(str(id(currentNode)), currentNode.value)
        #print("Ending Assignment")
        return currentNode

    def VisitPrintf(self, currentNode):
        #print("Beginning Printf")
        self.ast.node(str(id(currentNode)), currentNode.value)
        '''
        for child in currentNode.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)))
        '''
        form = currentNode.format.accept(self)
        self.ast.edge(str(id(currentNode)), str(id(form)), "Format")
        #print(currentNode.args)
        '''
        if currentNode.args:
            for child in currentNode.args.children:
                print("PRINTING NODE")
                node = child.accept(self)
                self.ast.edge(str(id(currentNode)), str(id(node)), "Args")
        '''
        if currentNode.args:
            for child in currentNode.args:
                #print("PRINTING NODE")
                #print(child)
                node = child.accept(self)
                self.ast.edge(str(id(currentNode)), str(id(node)), "Args")
        #print("Ending Printf")
        return currentNode

    def VisitScanf(self, currentNode):
        #print("Beginning Printf")
        self.ast.node(str(id(currentNode)), currentNode.value)
        form = currentNode.format.accept(self)
        self.ast.edge(str(id(currentNode)), str(id(form)), "Format")
        for child in currentNode.args.children:
            node = child.accept(self)
            self.ast.edge(str(id(currentNode)), str(id(node)), "Args")
        #print("Ending Printf")
        return currentNode
