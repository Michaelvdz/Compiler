import ast

from CGrammarVisitor import CGrammarVisitor
from CGrammarParser import CGrammarParser
from AST import *

class CSTVisitor(CGrammarVisitor):

    def __init__(self, tree):
        self.tree = tree
        self.stack = []
        print("Visiting the program")

    def visitProg(self, ctx):
        print("Prog")
        print("#children: " + str(ctx.getChildCount()))
        self.tree.Name = "Prog" + str(ctx.getRuleIndex())
        print("Visiting Prog children")
        prog = ASTNode("Prog")
        for child in ctx.children:
            node = self.visit(child)
            if isinstance(node, ASTNode):
                print("Printing:")
                prog.adopt(node)
        self.tree.setRoot(prog)
        print("Printing whole tree: ")
        self.tree.print()
        print("Done visiting Prog children")


    def visitInstr(self, ctx):
        print("Inst")
        print("#children: " + str(ctx.getChildCount()))
        instr = ASTNode("Inst")
        for child in ctx.children:
            node = self.visit(child)
            if isinstance(node, ASTNode):
                node.print()
                instr.adopt(node)
        return instr

    # Visit a parse tree produced by CGrammarParser#unary_operator.
    def visitUnary_operator(self, ctx: CGrammarParser.Unary_operatorContext):
        print("UnaryOperator")
        op = UnaryOperator(ctx.getText())
        op.print()
        return op

    # Visit a parse tree produced by CGrammarParser#parenthesis_expression.
    def visitParenthesis_expression(self, ctx: CGrammarParser.Parenthesis_expressionContext):
        print("ParenthesisExpression")
        print("--------------------------------------------")
        if len(ctx.children) == 3:
            for child in ctx.children:
                if not child.getText() == '(' and not child.getText() == ')':
                    print("No parenthesis")
                    node = self.visit(child)
                    return node
                else:
                    print(child)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#unary_expression.
    def visitUnary_expression(self, ctx: CGrammarParser.Unary_expressionContext):
        print("UnaryExpression")
        print("#children: " + str(ctx.getChildCount()))
        if len(ctx.children) == 2:
            newnode = UnaryOperation("")
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, UnaryOperator):
                    print("This is an operator")
                    newnode.value = node.value
                elif node is None:
                    newvar = ASTNode(ctx.iden.text)
                    newnode.adopt(newvar)
                else:
                    newnode.adopt(node)
            return newnode
        else:
            if ctx.iden:
                print("Id")
                var = ASTNode(ctx.getText())
                return var
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#mul_div_expression.
    def visitMul_div_expression(self, ctx: CGrammarParser.Mul_div_expressionContext):
        print("MulDivExpression")
        print("#children: " + str(ctx.getChildCount()))
        if ctx.getChildCount() > 1:
            binOp = BinaryOperation(ctx.op.text)
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    node.print()
                    binOp.adopt(node)
            binOp.print()
            return binOp
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#add_sub_expression.
    def visitAdd_sub_expression(self, ctx: CGrammarParser.Add_sub_expressionContext):
        print("AddSubExpression")
        print("#children: " + str(ctx.getChildCount()))
        if ctx.getChildCount() > 1:
            binOp = BinaryOperation(ctx.op.text)
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    node.print()
                    binOp.adopt(node)
            binOp.print()
            return binOp
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#relational_expression.
    def visitRelational_expression(self, ctx: CGrammarParser.Relational_expressionContext):
        print("RelationalExpression")
        print("#children: " + str(ctx.getChildCount()))
        if ctx.getChildCount() > 1:
            relOp = RelationOperation(ctx.op.text)
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    node.print()
                    relOp.adopt(node)
            relOp.print()
            return relOp
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#logical_expression.
    def visitLogical_expression(self, ctx: CGrammarParser.Logical_expressionContext):
        print("LogicalExpression")
        if ctx.getChildCount() > 1:
            logOp = LogicalOperation(ctx.op.text)
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    node.print()
                    logOp.adopt(node)
            logOp.print()
            return logOp
        else:
            return self.visitChildren(ctx)

    def visitAssignment_expression(self, ctx:CGrammarParser.Assignment_expressionContext):
        return self.visitChildren(ctx)


    def visitDeclaration_specification(self, ctx:CGrammarParser.Declaration_specificationContext):
        print("DeclarationSpecifier")
        decl = Declaration("VariableDeclartion")
        for child in ctx.children:
            node = self.visit(child)
            if isinstance(node, ASTNode):
                node.print()
                decl.adopt(node)
                decl.type = node
            elif str(child) == '*':
                pointer = ASTNode("*")
                decl.adopt(pointer)
            else:
                var = ASTNode(ctx.var.text)
                decl.adopt(var)
                decl.var = var
        return decl

    def visitDeclaration(self, ctx:CGrammarParser.DeclarationContext):
        print("Declaration")
        if ctx.assign:
            print("Assigment")
            print("#children: " + str(ctx.getChildCount()))
            assign = Assigment(ctx.assign.text)
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    assign.adopt(node)
            return assign
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#expr.
    def visitExpr(self, ctx: CGrammarParser.ExprContext):
        print("Expr")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#constant.
    def visitConstant(self, ctx: CGrammarParser.ConstantContext):
        print("Constant")
        const = Constant(ctx.getText())
        return const

    # Visit a parse tree produced by CGrammarParser#type.
    def visitType(self, ctx:CGrammarParser.TypeContext):
        print("Type")
        type = ASTNode("VariableType")
        for child in ctx.children:
            node = self.visit(child)
            if isinstance(node, ASTNode):
                node.print()
                type.adopt(node)
            else:
                print(child)
                type.name = str(child)
        return type


    # Visit a parse tree produced by CGrammarParser#reserved_word.
    def visitReserved_word(self, ctx:CGrammarParser.Reserved_wordContext):
        print("ReservedWord")
        word = ASTNode(ctx.getText())
        return word
