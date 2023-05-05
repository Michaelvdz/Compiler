import copy
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
    if "/" in filename:
        split = filename.split("/")
        size = len(split)
        filename2 = split[size-1]
        filename = filename2

    if len(argv) >=3 and argv[2]:
        outputmap = argv[2]
    else:
        outputmap = ""

    input_stream = FileStream(argv[1])
    lexer = CGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CGrammarParser(stream)
    #parser.addErrorListener(errorAnalyser())

    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() == 0:

        print("Creating AST")
        asttree = ASTTree()
        visitor = CSTVisitor(asttree)
        visitor.visit(tree)

        print("Printing tree before optimization")
        astVisitor = ASTVisitor(filename+"_beforeOptimization",outputmap)
        asttree.root.accept(astVisitor)
        #print("ending")
        astVisitor.ast.view()

        #Optimize tree
        optimizedTree = ASTTree()
        astOptimizer = ASTOptimizer(optimizedTree)
        optimizedTree.root = asttree.root.accept(astOptimizer)

        #optimizedTree = asttree


        print("Creating STS")
        #print("SymbolTable Part")
        STStack = SymbolTables()
        STCreator = CreateSymbolTableVisitor(STStack)
        optimizedTree.root.accept(STCreator)
        #print("\n\nThe generated symbol table:")
        #print(table)


        ErrorAnalyser = errorAnalyser(STStack.tables[0])
        optimizedTree.root.accept(ErrorAnalyser)

        print("-------------------------------")
        print(STStack.tables[0].name)
        print(len(STStack.tables[0].children))
        STStack.tables[0].print()
        print("-------------------------------")

        #print("Printing tree")
        astVisitor = ASTVisitor(filename, outputmap)
        optimizedTree.root.accept(astVisitor)
        #print("ending")
        astVisitor.ast.view()


        print("------- Creating LLVM IR -------")
        ST = copy.copy(STStack.tables[0])
        llvm = ""
        LLVMCreator = AST2LLVMVisitor(llvm, STStack.tables[0])
        optimizedTree.root.accept(LLVMCreator)
        #print(LLVMCreator.llvm)
        if outputmap != "":
            outputmap += "/"
        llvm = open(outputmap + filename+".ll", "w")
        llvm.write(LLVMCreator.llvm)
        llvm.close()

    else:
        print("Compiler interrupted after finding syntax errors")


if __name__ == '__main__':
    main(sys.argv)
