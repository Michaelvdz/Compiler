# Generated from CGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CGrammarParser import CGrammarParser
else:
    from CGrammarParser import CGrammarParser

# This class defines a complete generic visitor for a parse tree produced by CGrammarParser.

class CGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CGrammarParser#prog.
    def visitProg(self, ctx:CGrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#instr.
    def visitInstr(self, ctx:CGrammarParser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#unary_operator.
    def visitUnary_operator(self, ctx:CGrammarParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#parenthesis_expression.
    def visitParenthesis_expression(self, ctx:CGrammarParser.Parenthesis_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#unary_expression.
    def visitUnary_expression(self, ctx:CGrammarParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#mul_div_expression.
    def visitMul_div_expression(self, ctx:CGrammarParser.Mul_div_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#add_sub_expression.
    def visitAdd_sub_expression(self, ctx:CGrammarParser.Add_sub_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#relational_expression.
    def visitRelational_expression(self, ctx:CGrammarParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#logical_expression.
    def visitLogical_expression(self, ctx:CGrammarParser.Logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#expr.
    def visitExpr(self, ctx:CGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#constant.
    def visitConstant(self, ctx:CGrammarParser.ConstantContext):
        return self.visitChildren(ctx)



del CGrammarParser