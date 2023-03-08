# Generated from CGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CGrammarParser import CGrammarParser
else:
    from CGrammarParser import CGrammarParser

# This class defines a complete listener for a parse tree produced by CGrammarParser.
class CGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by CGrammarParser#prog.
    def enterProg(self, ctx:CGrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by CGrammarParser#prog.
    def exitProg(self, ctx:CGrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by CGrammarParser#instr.
    def enterInstr(self, ctx:CGrammarParser.InstrContext):
        pass

    # Exit a parse tree produced by CGrammarParser#instr.
    def exitInstr(self, ctx:CGrammarParser.InstrContext):
        pass


    # Enter a parse tree produced by CGrammarParser#expr.
    def enterExpr(self, ctx:CGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by CGrammarParser#expr.
    def exitExpr(self, ctx:CGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by CGrammarParser#unaryOperator.
    def enterUnaryOperator(self, ctx:CGrammarParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by CGrammarParser#unaryOperator.
    def exitUnaryOperator(self, ctx:CGrammarParser.UnaryOperatorContext):
        pass



del CGrammarParser