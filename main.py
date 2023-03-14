import sys
from antlr4 import *
from CGrammarLexer import CGrammarLexer
from CGrammarListener import CGrammarListener
from CGrammarParser import CGrammarParser
from CSTVisitor import CSTVisitor
from AST import *
from ASTVisitor import ASTVisitor

class MyListener(CGrammarListener):
    def exitExpr(self, ctx):
        print("Oh, a key!")


def main(argv):

    input_stream = FileStream(argv[1])
    lexer = CGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CGrammarParser(stream)
    tree = parser.prog()
    asttree = ASTTree()
    visitor = CSTVisitor(asttree)
    visitor.visit(tree)

    asttree.print()
    astVisitor = ASTVisitor()
    asttree.root.accept(astVisitor)
    astVisitor.ast.view()


if __name__ == '__main__':
    main(sys.argv)