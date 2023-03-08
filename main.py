import sys
from antlr4 import *
from CGrammarLexer import CGrammarLexer
from CGrammarListener import CGrammarListener
from CGrammarParser import CGrammarParser
from MyCVisitor import MyVisitor

class MyListener(CGrammarListener):
    def exitExpr(self, ctx):
        print("Oh, a key!")


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CGrammarParser(stream)
    tree = parser.prog()

    """
    print(tree.toStringTree())
    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    """
    tree
    visitor = MyVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)