import os
from main import *

currentPath = os.getcwd()
testPath = os.getcwd() + "/video/"
outputPath = os.getcwd() + "/videocompiled/"
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

    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() == 0:

        # print("Creating AST")
        asttree = ASTTree()
        visitor = CSTVisitor(asttree)
        visitor.visit(tree)

        #print("Printing tree before optimization")
        astVisitor = ASTVisitor(filename + "_beforeOptimization", "videocompiled/dot/")
        asttree.root.accept(astVisitor)
        astVisitor.ast.render()
        # print("ending")
        #astVisitor.ast.view()

        # Optimize tree
        optimizedTree = ASTTree()
        astOptimizer = ASTOptimizer(optimizedTree)
        optimizedTree.root = asttree.root.accept(astOptimizer)

        # optimizedTree = asttree

        #print("Creating STS")
        # print("SymbolTable Part")
        STStack = SymbolTables()
        STCreator = CreateSymbolTableVisitor(STStack)
        optimizedTree.root.accept(STCreator)

        # SACreator = SemanticAnalysisVisitor()
        # optimizedTree.root.accept(SACreator)

        # print("\n\nThe generated symbol table:")
        # print(table)

        ErrorAnalyser = errorAnalyser(STStack.tables[0])
        optimizedTree.root.accept(ErrorAnalyser)
        if ErrorAnalyser.errors == 0:
            print("-------------- Generated Symbol tables -----------------")
            STStack.tables[0].print()
            print("--------------------------------------------------------")

            # print("Printing tree")
            astVisitor = ASTVisitor(filename, "videocompiled/dot/")
            optimizedTree.root.accept(astVisitor)
            astVisitor.ast.render()
            # print("ending")
            #astVisitor.ast.view()

            # print("------- Creating LLVM IR -------")
            ST = copy.copy(STStack.tables[0])
            llvm = ""
            data = ""
            LLVMCreator = AST2MIPSVisitor(llvm, data, STStack.tables[0])
            optimizedTree.root.accept(LLVMCreator)
            # print(LLVMCreator.llvm)
            llvm = data + llvm
            llvm = open("videocompiled/" + filename + ".asm", "w")
            llvm.write(LLVMCreator.data+LLVMCreator.llvm)
            llvm.close()
            print(
                "\n" + Fore.GREEN + "Compiler succeeded compiling " + filename + " with " + Fore.MAGENTA + str(
                    ErrorAnalyser.warnings) + " warning(s)" + Fore.RESET + "\n")
        else:
            print(
                "\n" + Fore.RED + "Compiler failed compiling " + filename + " with " + str(
                    ErrorAnalyser.errors) + " error(s)" + Fore.RESET + "\n")

    else:
        print("Compiler interrupted after finding syntax errors")
