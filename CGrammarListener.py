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


    # Enter a parse tree produced by CGrammarParser#unary_operator.
    def enterUnary_operator(self, ctx:CGrammarParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by CGrammarParser#unary_operator.
    def exitUnary_operator(self, ctx:CGrammarParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by CGrammarParser#parenthesis_expression.
    def enterParenthesis_expression(self, ctx:CGrammarParser.Parenthesis_expressionContext):
        pass

    # Exit a parse tree produced by CGrammarParser#parenthesis_expression.
    def exitParenthesis_expression(self, ctx:CGrammarParser.Parenthesis_expressionContext):
        pass


    # Enter a parse tree produced by CGrammarParser#unary_expression.
    def enterUnary_expression(self, ctx:CGrammarParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by CGrammarParser#unary_expression.
    def exitUnary_expression(self, ctx:CGrammarParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by CGrammarParser#mul_div_expression.
    def enterMul_div_expression(self, ctx:CGrammarParser.Mul_div_expressionContext):
        pass

    # Exit a parse tree produced by CGrammarParser#mul_div_expression.
    def exitMul_div_expression(self, ctx:CGrammarParser.Mul_div_expressionContext):
        pass


    # Enter a parse tree produced by CGrammarParser#add_sub_expression.
    def enterAdd_sub_expression(self, ctx:CGrammarParser.Add_sub_expressionContext):
        pass

    # Exit a parse tree produced by CGrammarParser#add_sub_expression.
    def exitAdd_sub_expression(self, ctx:CGrammarParser.Add_sub_expressionContext):
        pass


    # Enter a parse tree produced by CGrammarParser#relational_expression.
    def enterRelational_expression(self, ctx:CGrammarParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by CGrammarParser#relational_expression.
    def exitRelational_expression(self, ctx:CGrammarParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by CGrammarParser#logical_expression.
    def enterLogical_expression(self, ctx:CGrammarParser.Logical_expressionContext):
        pass

    # Exit a parse tree produced by CGrammarParser#logical_expression.
    def exitLogical_expression(self, ctx:CGrammarParser.Logical_expressionContext):
        pass


    # Enter a parse tree produced by CGrammarParser#assignment_expression.
    def enterAssignment_expression(self, ctx:CGrammarParser.Assignment_expressionContext):
        pass

    # Exit a parse tree produced by CGrammarParser#assignment_expression.
    def exitAssignment_expression(self, ctx:CGrammarParser.Assignment_expressionContext):
        pass


    # Enter a parse tree produced by CGrammarParser#declaration_specification.
    def enterDeclaration_specification(self, ctx:CGrammarParser.Declaration_specificationContext):
        pass

    # Exit a parse tree produced by CGrammarParser#declaration_specification.
    def exitDeclaration_specification(self, ctx:CGrammarParser.Declaration_specificationContext):
        pass


    # Enter a parse tree produced by CGrammarParser#declaration.
    def enterDeclaration(self, ctx:CGrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CGrammarParser#declaration.
    def exitDeclaration(self, ctx:CGrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CGrammarParser#expr.
    def enterExpr(self, ctx:CGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by CGrammarParser#expr.
    def exitExpr(self, ctx:CGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by CGrammarParser#constant.
    def enterConstant(self, ctx:CGrammarParser.ConstantContext):
        pass

    # Exit a parse tree produced by CGrammarParser#constant.
    def exitConstant(self, ctx:CGrammarParser.ConstantContext):
        pass


    # Enter a parse tree produced by CGrammarParser#type.
    def enterType(self, ctx:CGrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by CGrammarParser#type.
    def exitType(self, ctx:CGrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by CGrammarParser#reserved_word.
    def enterReserved_word(self, ctx:CGrammarParser.Reserved_wordContext):
        pass

    # Exit a parse tree produced by CGrammarParser#reserved_word.
    def exitReserved_word(self, ctx:CGrammarParser.Reserved_wordContext):
        pass


    # Enter a parse tree produced by CGrammarParser#comment.
    def enterComment(self, ctx:CGrammarParser.CommentContext):
        pass

    # Exit a parse tree produced by CGrammarParser#comment.
    def exitComment(self, ctx:CGrammarParser.CommentContext):
        pass


    # Enter a parse tree produced by CGrammarParser#printf.
    def enterPrintf(self, ctx:CGrammarParser.PrintfContext):
        pass

    # Exit a parse tree produced by CGrammarParser#printf.
    def exitPrintf(self, ctx:CGrammarParser.PrintfContext):
        pass



del CGrammarParser