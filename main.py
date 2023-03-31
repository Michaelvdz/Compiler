import sys

import os
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

    filename = argv[1]
    filename = os.path.splitext(filename)[0]

    input_stream = FileStream(argv[1])
    lexer = CGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CGrammarParser(stream)
    parser.addErrorListener(errorAnalyser())

    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() == 0:

        asttree = ASTTree()
        visitor = CSTVisitor(asttree)
        visitor.visit(tree)

        #print("Printing tree before optimization")
        astVisitor = ASTVisitor(filename+"_beforeOptimization")
        asttree.root.accept(astVisitor)
        #print("ending")
        astVisitor.ast.view()

        #Optimize tree
        optimizedTree = ASTTree()
        astOptimizer = ASTOptimizer(optimizedTree)
        optimizedTree.root = asttree.root.accept(astOptimizer)

        #optimizedTree = asttree



        #print("SymbolTable Part")
        table = SymbolTable()
        STCreator = CreateSymbolTableVisitor(table)
        optimizedTree.root.accept(STCreator)
        #print("\n\nThe generated symbol table:")
        #print(table)


        #print("Printing tree")
        astVisitor = ASTVisitor(filename)
        optimizedTree.root.accept(astVisitor)
        #print("ending")
        astVisitor.ast.view()

        llvm = ""
        llvm += "define dso_local i32 @main(){\n"
        LLVMCreator = AST2LLVMVisitor(llvm, table)
        optimizedTree.root.accept(LLVMCreator)
        LLVMCreator.llvm += "ret i32 0\n}"
        #print(LLVMCreator.llvm)

        llvm = open(filename+".ll", "w")
        llvm.write(LLVMCreator.llvm)
        llvm.close()

    else:
        print("Compiler interrupted after finding syntax errors")





if __name__ == '__main__':
    main(sys.argv)
