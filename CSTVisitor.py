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
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#parenthesis_expression.
    def visitParenthesis_expression(self, ctx: CGrammarParser.Parenthesis_expressionContext):
        print("ParenthesisExpression")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#unary_expression.
    def visitUnary_expression(self, ctx: CGrammarParser.Unary_expressionContext):
        print("UnaryExpression")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#mul_div_expression.
    def visitMul_div_expression(self, ctx: CGrammarParser.Mul_div_expressionContext):
        print("MulDivExpression")
        if ctx.getChildCount() > 1:
            binOp = BinaryOperation(ctx.op)
            self.stack.append(binOp)
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
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#logical_expression.
    def visitLogical_expression(self, ctx: CGrammarParser.Logical_expressionContext):
        print("LogicalExpression")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#expr.
    def visitExpr(self, ctx: CGrammarParser.ExprContext):
        print("Expr")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#constant.
    def visitConstant(self, ctx: CGrammarParser.ConstantContext):
        #print("Constant")
        const = Constant(ctx.getText())
        return const

