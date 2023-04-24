import os
from main import *

currentPath = os.getcwd()
testPath = os.getcwd() + "/testfiles4/"
outputPath = os.getcwd() + "/outputfiles4/"
print(testPath)
STStack = SymbolTables()
files = os.listdir(testPath)
i = 0

print("Compiling files:")
for file in files:
    STStack.empty()
    print(file)
    filename = os.path.splitext(file)[0]
    input_stream = FileStream(testPath+file)
    lexer = CGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CGrammarParser(stream)
    parser.addErrorListener(errorAnalyser())

    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() == 0:

        # Convert CST to AST
        asttree = ASTTree()
        visitor = CSTVisitor(asttree)
        visitor.visit(tree)

        # Print before optimization
        astVisitor = ASTVisitor(filename+"_beforeOptimization", "outputfiles4")
        asttree.root.accept(astVisitor)
        astVisitor.ast.render()

        # Optimize tree
        optimizedTree = ASTTree()
        astOptimizer = ASTOptimizer(optimizedTree)
        optimizedTree.root = asttree.root.accept(astOptimizer)

        # Create symbol table
        print("Creating STS")
        print(STStack)
        STCreator = CreateSymbolTableVisitor(STStack)
        optimizedTree.root.accept(STCreator)
        STStack.tables[0].print()

        # Print after optimisation
        astVisitor = ASTVisitor(filename, "outputfiles")
        optimizedTree.root.accept(astVisitor)
        astVisitor.ast.render()

        # Generate llvm
        #ST = copy.copy(STStack.tables[0])
        llvm = ""
        LLVMCreator = AST2LLVMVisitor(llvm, STStack.tables[0])
        optimizedTree.root.accept(LLVMCreator)
        # Act like we are close the main function for future debugging
        LLVMCreator.printing = False
        llvm = open(outputPath+filename+".ll", "w")
        llvm.write(LLVMCreator.llvm)
        llvm.close()
        i+= 1
    else:
        print("Compiler interrupted after finding syntax errors")
