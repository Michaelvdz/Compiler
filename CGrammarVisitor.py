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


    # Visit a parse tree produced by CGrammarParser#post_unary_operator.
    def visitPost_unary_operator(self, ctx:CGrammarParser.Post_unary_operatorContext):
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


    # Visit a parse tree produced by CGrammarParser#assignment_expression.
    def visitAssignment_expression(self, ctx:CGrammarParser.Assignment_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#pointer.
    def visitPointer(self, ctx:CGrammarParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#declaration_specification.
    def visitDeclaration_specification(self, ctx:CGrammarParser.Declaration_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#declaration.
    def visitDeclaration(self, ctx:CGrammarParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#expr.
    def visitExpr(self, ctx:CGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#expr_loop.
    def visitExpr_loop(self, ctx:CGrammarParser.Expr_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#argumentlist.
    def visitArgumentlist(self, ctx:CGrammarParser.ArgumentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#identifierlist.
    def visitIdentifierlist(self, ctx:CGrammarParser.IdentifierlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#parameterlist.
    def visitParameterlist(self, ctx:CGrammarParser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#function.
    def visitFunction(self, ctx:CGrammarParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#conditional_statement.
    def visitConditional_statement(self, ctx:CGrammarParser.Conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#loops.
    def visitLoops(self, ctx:CGrammarParser.LoopsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#jumps.
    def visitJumps(self, ctx:CGrammarParser.JumpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#scope.
    def visitScope(self, ctx:CGrammarParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#constant.
    def visitConstant(self, ctx:CGrammarParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#type.
    def visitType(self, ctx:CGrammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#type_specifier.
    def visitType_specifier(self, ctx:CGrammarParser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#reserved_word.
    def visitReserved_word(self, ctx:CGrammarParser.Reserved_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#comment.
    def visitComment(self, ctx:CGrammarParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#printf.
    def visitPrintf(self, ctx:CGrammarParser.PrintfContext):
        return self.visitChildren(ctx)



del CGrammarParser