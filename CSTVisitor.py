import ast
import re
from CGrammarVisitor import CGrammarVisitor
from CGrammarParser import CGrammarParser
from AST import *

class CSTVisitor(CGrammarVisitor):

    def __init__(self, tree):
        self.tree = tree
        self.stack = []
        #print("Visiting the program")

    def visitProg(self, ctx):
        print("Prog")
        #print("#children: " + str(ctx.getChildCount()))
        self.tree.Name = "Prog" + str(ctx.getRuleIndex())
        #print("Visiting Prog children")
        prog = ASTNode("Prog")
        for child in ctx.children:
            node = self.visit(child)
            if isinstance(node, ASTNode):
                #print("Printing:")
                prog.adopt(node)
        self.tree.setRoot(prog)
        #print("Printing whole tree: ")
        #self.tree.print()
        #print("Done visiting Prog children")


    def visitInstr(self, ctx):
        print("Inst")
        #print("#children: " + str(ctx.getChildCount()))
        instr = ASTNode("Inst")
        '''
        if ctx.bc:
            comment = MLComment(ctx.bc.text)
            instr.adopt(comment)
        else:
        '''
        for child in ctx.children:
            node = self.visit(child)
            print("Node recieved from child")
            print(node)
            if isinstance(node, ASTNode):
                #node.print()
                instr.adopt(node)
        return instr

    # Visit a parse tree produced by CGrammarParser#unary_operator.
    def visitUnary_operator(self, ctx: CGrammarParser.Unary_operatorContext):
        #print("UnaryOperator")
        op = UnaryOperator(ctx.getText())
        #op.print()
        return op

    # Visit a parse tree produced by CGrammarParser#unary_operator.
    def visitPost_unary_operator(self, ctx: CGrammarParser.Unary_operatorContext):
        #print("PostUnaryOperator")
        op = UnaryOperator(ctx.getText())
        #op.print()
        return op

    # Visit a parse tree produced by CGrammarParser#parenthesis_expression.
    def visitParenthesis_expression(self, ctx: CGrammarParser.Parenthesis_expressionContext):
        #print("ParenthesisExpression")
        #print("--------------------------------------------")
        if len(ctx.children) == 3:
            for child in ctx.children:
                if not child.getText() == '(' and not child.getText() == ')':
                    #print("No parenthesis")
                    node = self.visit(child)
                    return node

        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#unary_expression.
    def visitUnary_expression(self, ctx: CGrammarParser.Unary_expressionContext):
        #print("UnaryExpression")
        #print("#children: " + str(ctx.getChildCount()))
        if len(ctx.children) == 2:
            newnode = UnaryOperation("")
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, UnaryOperator):
                    #print("This is an operator")
                    newnode.value = node.value
                elif node is None:
                    newvar = ASTNode(ctx.iden.text)
                    newnode.adopt(newvar)
                else:
                    newnode.adopt(node)
            return newnode
        else:
            if ctx.iden:
                #print("Id")
                var = ASTNode(ctx.getText())
                return var
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#mul_div_expression.
    def visitMul_div_expression(self, ctx: CGrammarParser.Mul_div_expressionContext):
        #print("MulDivExpression")
        #print("#children: " + str(ctx.getChildCount()))
        if ctx.getChildCount() > 1:
            binOp = BinaryOperation(ctx.op.text)
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    #node.print()
                    binOp.adopt(node)
            #binOp.print()
            return binOp
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#add_sub_expression.
    def visitAdd_sub_expression(self, ctx: CGrammarParser.Add_sub_expressionContext):
        #print("AddSubExpression")
        #print("#children: " + str(ctx.getChildCount()))
        if ctx.getChildCount() > 1:
            binOp = BinaryOperation(ctx.op.text)
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    #node.print()
                    binOp.adopt(node)
            #binOp.print()
            return binOp
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#relational_expression.
    def visitRelational_expression(self, ctx: CGrammarParser.Relational_expressionContext):
        #print("RelationalExpression")
        #print("#children: " + str(ctx.getChildCount()))
        if ctx.getChildCount() > 1:
            relOp = BinaryOperation(ctx.op.text)
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    #node.print()
                    relOp.adopt(node)
            #relOp.print()
            return relOp
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#logical_expression.
    def visitLogical_expression(self, ctx: CGrammarParser.Logical_expressionContext):
        #print("LogicalExpression")
        if ctx.getChildCount() > 1:
            logOp = BinaryOperation(ctx.op.text)
            for child in ctx.children:
                node = self.visit(child)

                if isinstance(node, ASTNode):
                    #node.print()
                    logOp.adopt(node)
            #logOp.print()
            return logOp
        else:
            return self.visitChildren(ctx)

    def visitAssignment_expression(self, ctx:CGrammarParser.Assignment_expressionContext):
        return self.visitChildren(ctx)


    def visitDeclaration_specification(self, ctx:CGrammarParser.Declaration_specificationContext):
        print("DeclarationSpecifier")
        decl = Declaration("VariableDeclartion")
        decl.attr = ""
        '''
        if ctx.ptr:
            #print("Contains pointer")
            # lvalue contains a pointer, which can either be a declaration/definition or assignment
            if ctx.typ:
                # This is a declaration/definition
                for child in ctx.children:
                    node = self.visit(child)
                    #print("child:")
                    #print(ctx.var.text)
                    if isinstance(node, Variable):
                        for child2 in node.children:
                            if child2.type == "reserved_word":
                                decl.adopt(child2)
                                decl.attr = child2.value
                            if child2.type == "type":
                                #print("Doetem dees wel?")
                                decl.adopt(child2)
                                decl.type = child2.value + "*"
                                #print(decl.type)
                    elif child is ctx.ptr:
                        pointer = ASTNode("*")
                        decl.adopt(pointer)
                    else:
                        #print("test")
                        var = ASTNode(ctx.var.text)
                        decl.adopt(var)
                        decl.var = var.value
            else:
                # This is just an assignment to the value the pointer is pointing to
                #print("Zijn we hier")
                #print(self.visit(ctx.ptr).value)
                op = UnaryOperation(self.visit(ctx.ptr).value)
                var = ASTNode(ctx.var.text)
                op.adopt(var)
                return op

            #print(decl.var)
            #print(decl.type)
            #print(decl.attr)
            #print("Pointer declaration with:")
            #print("Varname: " + decl.var)
            #print("Type: " + decl.type)
            #print("Attr: " + decl.attr)
        else:
            # We are assigning a value to
            print("Declaring var not pointer")
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, Variable):
                    for child2 in node.children:
                        if child2.type == "reserved_word":
                            decl.adopt(child2)
                            decl.attr = child2.value
                        if child2.type == "type":
                            decl.adopt(child2)
                            decl.type = child2.value
                elif str(child) == '*':
                    pointer = ASTNode("*")
                    decl.adopt(pointer)
                else:
                    var = ASTNode(ctx.var.text)
                    decl.adopt(var)
                    decl.var = var.value
        '''
        # Test for declaration/definition or just var assignment
        if ctx.typ:
            # We are in decl/def
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, Variable):
                    for child2 in node.children:
                        if child2.type == "reserved_word":
                            decl.adopt(child2)
                            decl.attr = child2.value
                        if child2.type == "type":
                            # print("Doetem dees wel?")
                            decl.adopt(child2)
                            if ctx.ptr:
                                # We are in pointer decl/def
                                decl.type = child2.value + "*"
                            else:
                                decl.type = child2.value
                elif child is ctx.ptr:
                    pointer = ASTNode("*")
                    decl.adopt(pointer)
                else:
                    # print("test")
                    var = ASTNode(ctx.var.text)
                    decl.adopt(var)
                    decl.var = var.value
        else:
            # We are just in var assignment/definition
            if ctx.ptr:
                op = UnaryOperation(self.visit(ctx.ptr).value)
                var = ASTNode(ctx.var.text)
                op.adopt(var)
                return op
            else:
                for child in ctx.children:
                    node = self.visit(child)
                    var = Variable(ctx.var.text)
                    #decl.adopt(var)
                    #decl.var = var.value
                    return var
        # We return decl if we have a declaration
        return decl

    def visitDeclaration(self, ctx:CGrammarParser.DeclarationContext):
        print("Declaration")
        if ctx.assign:
            assign = Assigment(ctx.assign.text)
            assign.rvalue = self.visit(ctx.rvalue)
            assign.lvalue = self.visit(ctx.lvalue)
            assign.adopt(assign.lvalue)
            assign.adopt(assign.rvalue)
            return assign
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#expr.
    def visitExpr(self, ctx: CGrammarParser.ExprContext):
        print("Expr")
        for child in ctx.children:
            if not child.getText() == ";":
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    return node
        return node

    # Visit a parse tree produced by CGrammarParser#conditional_statement.
    def visitConditional_statement(self, ctx:CGrammarParser.Conditional_statementContext):
        print("Conditional")
        node = Conditional("Conditional")
        condition = self.visit(ctx.condition)
        node.adopt(condition)
        node.condition = condition
        ifbody = self.visit(ctx.ifbody)
        node.ifbody = ifbody
        node.adopt(ifbody)
        if ctx.elsebody:
            elsebody = self.visit(ctx.elsebody)
            node.adopt(elsebody)
            node.elsebody = elsebody
        return node


    # Visit a parse tree produced by CGrammarParser#loops.
    def visitLoops(self, ctx:CGrammarParser.LoopsContext):
        print("Loop")
        node = ASTNode("Loop")
        for child in ctx.content:
            childnode = self.visit(child)
            node.adopt(childnode)
        return node


    # Visit a parse tree produced by CGrammarParser#scope.
    def visitScope(self, ctx:CGrammarParser.ScopeContext):
        print("Scope")
        node = Scope("UnnamedScope")
        for child in ctx.children:
            if not child.getText() == "{" and not child.getText() == "}":
                childnode = self.visit(child)
                node.adopt(childnode)
        return node


    # Visit a parse tree produced by CGrammarParser#constant.
    def visitConstant(self, ctx: CGrammarParser.ConstantContext):
        #print("Constant")
        const = Constant(ctx.getText())
        return const

    # Visit a parse tree produced by CGrammarParser#type.
    def visitType(self, ctx:CGrammarParser.TypeContext):
        #print("Type")
        type = Variable("Variable")
        for child in ctx.children:
            node = self.visit(child)
            if isinstance(node, ASTNode):
                type.adopt(node)
            else:
                type.name = str(child)
        #print("EndOfType")
        return type

    def visitType_specifier(self, ctx:CGrammarParser.Reserved_wordContext):
        #print("TypeSpecifier")
        #print("Type")
        #print(ctx.typ.text)
        type = ASTNode(ctx.typ.text)
        type.type = "type"
        #print("EndOfTypeSpecifier")
        return type

    # Visit a parse tree produced by CGrammarParser#reserved_word.
    def visitReserved_word(self, ctx:CGrammarParser.Reserved_wordContext):
        #print("ReservedWord")
        word = ASTNode(ctx.getText())
        word.type = "reserved_word"
        return word

    # Visit a parse tree produced by CGrammarParser#reserved_word.
    def visitPointer(self, ctx:CGrammarParser.Reserved_wordContext):
        #print("Pointer")
        word = ASTNode(ctx.getText())
        word.type = "pointer"
        return word

    # Visit a parse tree produced by CGrammarParser#reserved_word.
    def visitComment(self, ctx: CGrammarParser.CommentContext):
        #print("Comment--------------------------")
        if ctx.block:
            comment = MLComment(ctx.block.text)
        elif ctx.sl:
            comment = SLComment(ctx.sl.text)
        return comment

    def visitPrintf(self, ctx: CGrammarParser.PrintfContext):
        print("Printf")
        result = re.search('\((.+?)\)', ctx.getText()).group(1)
        #print("need this")
        #print(result)
        node = ASTNode(result)
        printf = PrintF("printf()")
        printf.adopt(node)
        return printf
