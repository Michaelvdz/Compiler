from antlr4 import *
from CGrammarParser import CGrammarParser
from CGrammarVisitor import CGrammarVisitor
from SymbolTable import SymbolTable 

class VisitorST(CGrammarVisitor):
    def __init__(self):
        self.symtable = SymbolTable()

    def visitDeclaration_specification(self, ctx: CGrammarParser.DeclarationContext):
        varName = ctx.getText()
        varType = ctx.getText()

        self.symtable.insertTable(varName, varType)
