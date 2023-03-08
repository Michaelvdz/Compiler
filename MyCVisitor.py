from MyGrammarVisitor import MyGrammarVisitor
from MyGrammarParser import MyGrammarParser

class MyVisitor(MyGrammarVisitor):
    def __init__(self):
        self.memory = {}

    def visitProg(self, ctx):
        print(ctx.toStringTree())
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        print("test")
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx):
        return ctx.INT().getText()

    def visitMulDiv(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == MyGrammarParser.MUL:
            return left * right
        return left / right

    def visitAddSub(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == MyGrammarParser.ADD:
            return left + right
        return left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())