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

    name = ""
    value = ""
    children = []
    type = ""
    line = 0
    column = 0
    def __init__(self, name="Free"):
        #print("___init-ASTNode___");
        self.children = []
        self.name = name
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

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
            #print("Adding node: " + node.name)
            self.children.append(node)

    def accept(self, visitor: Visitor):
        value = visitor.VisitASTNode(self)
        return value

    def acceptWithNoOptimization(self, visitor: Visitor):
        value = visitor.VisitASTNode(self, False)
        return value

class Array(ASTNode):

    name = ""
    value = ""
    children = []
    size = ""
    line = 0
    column = 0
    def __init__(self, name="Free"):
        #print("___init-ASTNode___");
        self.children = []
        self.name = name
        self.value = name
        self.size = ""
        #print("___Node-Created-With-Name:"+ self.name + "___")

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
            #print("Adding node: " + node.name)
            self.children.append(node)

    def accept(self, visitor: Visitor):
        value = visitor.VisitArray(self)
        return value


class BinaryOperation(ASTNode):

    name = ""
    children = []
    value = ""
    type = ""
    line = 0
    column = 0

    def __init__(self, name):
        #print("___init-BinaryOperation___");
        self.children = []
        self.name = "BinaryOperation"
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            #print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a binary operation node with operator: " + str(self.value) + " and nodes:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitBinaryOperation(self)

class Scope(ASTNode):

    name = ""
    children = []
    value = ""
    line = 0
    column = 0

    def __init__(self, name):
        #print("___init-BinaryOperation___");
        self.children = []
        self.name = "Scope"
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            #print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a scope node with name: " + str(self.value) + " and nodes:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitScope(self)

class ExprLoop(ASTNode):

    name = ""
    children = []
    value = ""
    line = 0
    column = 0

    def __init__(self, name):
        #print("___init-BinaryOperation___");
        self.children = []
        self.name = "ExprLoop"
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            #print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a ExprLoop node with name: " + str(self.value) + " and nodes:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitExprLoop(self)

class Conditional(ASTNode):

    name = ""
    children = []
    value = ""
    condition = 0
    ifbody = 0
    elsebody = 0
    line = 0
    column = 0


    def __init__(self, name):
        #print("___init-BinaryOperation___");
        self.children = []
        self.name = "Conditional"
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            #print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a conditional node with name: " + str(self.value) + " and nodes:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitConditional(self)

class While(ASTNode):

    name = ""
    children = []
    value = ""
    condition = 0
    body = 0
    beforeLoop = 0
    afterLoop = 0
    line = 0
    column = 0


    def __init__(self, name):
        #print("___init-BinaryOperation___");
        self.children = []
        self.name = "While"
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            #print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a while node with name: " + str(self.value) + " and nodes:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitWhile(self)

class Jump(ASTNode):

    name = ""
    value = ""
    children = []
    type = ""
    line = 0
    column = 0
    
    def __init__(self, name="Free"):
        #print("___init-ASTNode___");
        self.children = []
        self.name = name
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

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
            #print("Adding node: " + node.name)
            self.children.append(node)

    def accept(self, visitor: Visitor):
        value = visitor.VisitJump(self)
        return value

    def acceptWithNoOptimization(self, visitor: Visitor):
        value = visitor.VisitASTNode(self, False)
        return value

class Function(ASTNode):

    name = ""
    value = ""
    returnType = ""
    hasbody = False
    body = []
    params = []
    children = []
    totalParams = 0
    line = 0
    column = 0
    
    def __init__(self, name="Free"):
        #print("___init-ASTNode___");
        self.children = []
        self.name = name
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

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
            #print("Adding node: " + node.name)
            self.children.append(node)

    def accept(self, visitor: Visitor):
        value = visitor.VisitFunction(self)
        return value

    def acceptWithNoOptimization(self, visitor: Visitor):
        value = visitor.VisitASTNode(self, False)
        return value

class UnaryOperation(ASTNode):

    name = ""
    children = []
    value = ""
    line = 0
    column = 0

    def __init__(self, name):
        #print("___init-UnaryOperation___");
        self.children = []
        self.name = "UnaryOperation"
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            #print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a unary.c operation node with operator: " + str(self.value) + " and nodes:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitUnaryOperation(self)

class Declaration(ASTNode):

    name = ""
    children = []
    value = ""
    type = ASTNode
    var = ASTNode
    attr = ASTNode
    pointer = ASTNode
    array = 0
    line = 0
    column = 0


    def __init__(self, name):
        #print("___init-Declaration___");
        self.children = []
        self.name = "Declaration"
        self.value = name
        self.pointer = None
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            #print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a declaration node:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitDeclaration(self)

    def acceptWithValue(self, visitor: Visitor, value=0):
        return visitor.VisitDeclaration(self, value)

class Pointer(ASTNode):

    name = ""
    children = []
    value = ""
    type = ASTNode
    var = ASTNode
    attr = ASTNode
    line = 0
    column = 0


    def __init__(self, name):
        #print("___init-Declaration___");
        self.children = []
        self.name = name
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            #print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a pointer node:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitPointer(self)


class Constant(ASTNode):

    name = ""
    children = []
    value = ""
    varName = ""
    varType = ""
    type = ""
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-Constant__");
        self.children = 0
        self.name = "Constant"
        self.value = value
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def print(self):
        print("Constant: " + str(self.value))

    def accept(self, visitor: Visitor):
        return visitor.VisitConstant(self)

class String(ASTNode):

    name = ""
    children = []
    value = ""
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-Constant__");
        self.children = 0
        self.name = "String"
        self.value = value
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def print(self):
        print("String: " + str(self.value))

    def accept(self, visitor: Visitor):
        return visitor.VisitString(self)

class PointerDeref(ASTNode):

    name = ""
    children = []
    variable = ASTNode

    rvalue = False
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-Variable__")
        self.children = []
        self.name = "PointerDeref"
        self.value = value
        #print("___Node-Created-With-Name:" + self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def print(self):
        print("Variable: " + str(self.value))

    def accept(self, visitor: Visitor):
        return visitor.VisitPointerDeref(self)

class Variable(ASTNode):

    name = ""
    children = []
    value = ""
    type = ""
    attr = ""
    rvalue = False
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-Variable__")
        self.children = []
        self.name = "Variable"
        self.value = value
        #print("___Node-Created-With-Name:" + self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def print(self):
        print("Variable: " + str(self.value))

    def accept(self, visitor: Visitor):
        return visitor.VisitVariable(self)

class ArrayVariable(ASTNode):

    name = ""
    children = []
    value = ""
    type = ""
    attr = ""
    lvalue = False
    index = ""
    size = ""
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-Variable__")
        self.children = []
        self.name = "ArrayVariable"
        self.value = value
        #print("___Node-Created-With-Name:" + self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def print(self):
        print("ArrayVariable: " + str(self.value))

    def accept(self, visitor: Visitor):
        return visitor.VisitArrayVariable(self)

class Call(ASTNode):

    name = ""
    children = []
    value = ""
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-Variable__")
        self.children = []
        self.name = "Call"
        self.value = value
        #print("___Node-Created-With-Name:" + self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def print(self):
        print("Variable: " + str(self.value))

    def accept(self, visitor: Visitor):
        return visitor.VisitCall(self)

class UnaryOperator(ASTNode):

    name = ""
    children = []
    value = ""
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-UnaryOperator__");
        self.children = []
        self.name = "Operator"
        self.value = value
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def print(self):
        print("Operator: " + self.value)

    def accept(self, visitor: Visitor):
        return visitor.VisitUnaryOperator(self)

class Assigment(ASTNode):

    name = ""
    children = []
    value = ""
    lvalue = ASTNode
    rvalue = ASTNode
    line = 0
    column = 0

    def __init__(self, name):
        #print("___init-Assigment___");
        self.children = []
        self.name = "RelationOperation"
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            #print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a assigment node with operator: " + str(self.value) + " and nodes:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitAssignment(self)

class MLComment(ASTNode):

    value = ""
    name = ""
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-MLComment__");
        self.children = 0
        self.name = "Comment"
        self.value = value
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def print(self):
        print("Comment: " + str(self.value))

    def accept(self, visitor: Visitor):
        return visitor.VisitMLComment(self)

class SLComment(ASTNode):

    value = ""
    name = ""
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-SLComment__");
        self.children = 0
        self.name = "Comment"
        self.value = value
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def print(self):
        print("Comment: " + str(self.value))

    def accept(self, visitor: Visitor):
        return visitor.VisitSLComment(self)

class Include(ASTNode):

    value = ""
    name = ""
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-SLComment__");
        self.children = 0
        self.name = "Include"
        self.value = value
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def print(self):
        print("Include: " + str(self.value))

    def accept(self, visitor: Visitor):
        return visitor.VisitInclude(self)

class PrintF(ASTNode):

    value = ""
    name = ""
    children = []
    format = ""
    args = []
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-Printf__");
        self.children = []
        self.name = "Printf"
        self.value = value
        self.format = ""
        self.args = []
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def print(self):
        print("Prinf: " + str(self.value))

    def accept(self, visitor: Visitor):
        return visitor.VisitPrintf(self)

    def adopt(self, node):
        self.children.append(node)

class ScanF(ASTNode):

    value = ""
    name = ""
    children = []
    format = ""
    args = []
    line = 0
    column = 0

    def __init__(self, value):
        #print("___init-Scanf__");
        self.children = []
        self.name = "Scanf"
        self.value = value
        self.format = ""
        self.args = []
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def print(self):
        print("Scanf: " + str(self.value))

    def accept(self, visitor: Visitor):
        return visitor.VisitScanf(self)

    def adopt(self, node):
        self.children.append(node)



'''
class RelationOperation(ASTNode):

    name = ""
    children = []
    value = ""

    def __init__(self, name):
        #print("___init-RelationOperation___");
        self.children = []
        self.name = "RelationOperation"
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a relation operation node with operator: " + str(self.value) + " and nodes:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitRelationOperation(self)

class LogicalOperation(ASTNode):

    name = ""
    children = []
    value = ""

    def __init__(self, name):
        #print("___init-LogicalOperation___");
        self.children = []
        self.name = "LogicalOperation"
        self.value = name
        #print("___Node-Created-With-Name:"+ self.name + "___")

    def adopt(self, node):
        self.children.append(node)

    def adoptChildren(self, nodes):
        for node in nodes:
            #print("Adding node: " + node.name)
            self.children.append(node)

    def print(self):
        print("This is a logical operation node with operator: " + str(self.value) + " and nodes:")
        for node in self.children:
            node.print()

    def accept(self, visitor: Visitor):
        return visitor.VisitLogicalOperation(self)
'''
