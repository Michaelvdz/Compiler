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


    # Visit a parse tree produced by CGrammarParser#expr.
    def visitExpr(self, ctx:CGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#unaryOperator.
    def visitUnaryOperator(self, ctx:CGrammarParser.UnaryOperatorContext):
        return self.visitChildren(ctx)



del CGrammarParser