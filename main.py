import sys

import SymbolTable
from antlr4 import *
from CGrammarLexer import CGrammarLexer
from CGrammarListener import CGrammarListener
from CGrammarParser import CGrammarParser
from CSTVisitor import CSTVisitor
from AST import *
from ASTVisitor import ASTVisitor
from CreateSymbolTableVisitor import CreateSymbolTableVisitor
from errorAnalysis import errorAnalyser
from ASTOptimizer import ASTOptimizer
from SymbolTable import *
from AST2LLVMVisitor import *

def main(argv):

    input_stream = FileStream(argv[1])
    lexer = CGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CGrammarParser(stream)
    parser.addErrorListener(errorAnalyser())
    tree = parser.prog()

    asttree = ASTTree()
    visitor = CSTVisitor(asttree)
    visitor.visit(tree)

    #Optimize tree

    optimizedTree = ASTTree()
    astOptimizer = ASTOptimizer(optimizedTree)
    optimizedTree.root = asttree.root.accept(astOptimizer)

    #optimizedTree = asttree

    print("Printing tree")
    astVisitor = ASTVisitor()
    optimizedTree.root.accept(astVisitor)
    print("ending")
    astVisitor.ast.view()

    print("SymbolTable Part")
    table = SymbolTable()
    STCreator = CreateSymbolTableVisitor(table)
    optimizedTree.root.accept(STCreator)
    print("\n\nThe generated symbol table:")
    print(table)


    print("Printing tree")
    astVisitor = ASTVisitor()
    optimizedTree.root.accept(astVisitor)
    print("ending")
    astVisitor.ast.view()
    #astVisitor.ast.view()

    llvm = ""
    LLVMCreator = AST2LLVMVisitor(llvm, table)
    optimizedTree.root.accept(LLVMCreator)
    print(LLVMCreator.llvm)
    print(table)




if __name__ == '__main__':
    main(sys.argv)
