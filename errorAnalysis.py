from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CGrammarLexer import CGrammarLexer
from CGrammarParser import CGrammarParser

import sys


class errorAnalyser(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Syntax Error!")
