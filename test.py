import os
from main import *

currentPath = os.getcwd()
testPath = os.getcwd() + "/testfiles/"
outputPath = os.getcwd() + "/outputfiles/"
print(testPath)

files = os.listdir(testPath)

print("Compiling files:")
for file in files:
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
        astVisitor = ASTVisitor(filename+"_beforeOptimization", "outputfiles")
        asttree.root.accept(astVisitor)
        astVisitor.ast.render()

        # Optimize tree
        optimizedTree = ASTTree()
        astOptimizer = ASTOptimizer(optimizedTree)
        optimizedTree.root = asttree.root.accept(astOptimizer)

        # Create symbol table
        table = SymbolTable()
        STCreator = CreateSymbolTableVisitor(table)
        optimizedTree.root.accept(STCreator)

        # Print after optimisation
        astVisitor = ASTVisitor(filename, "outputfiles")
        optimizedTree.root.accept(astVisitor)
        astVisitor.ast.render()

        # Generate llvm
        llvm = ""
        # Act like we are in the main function for future debugging
        llvm += "define dso_local i32 @main(){\n"
        LLVMCreator = AST2LLVMVisitor(llvm, table)
        optimizedTree.root.accept(LLVMCreator)
        # Act like we are close the main function for future debugging
        LLVMCreator.llvm += "ret i32 0\n}"
        LLVMCreator.printing = False

        llvm = open(outputPath+filename+".ll", "w")
        llvm.write(LLVMCreator.llvm)
        llvm.close()

    else:
        print("Compiler interrupted after finding syntax errors")
