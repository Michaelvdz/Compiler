C to MIPS Compiler
===================

This is a C to MIPS Compiler for the Compilers course taught
at the University of Antwerp.

We started this project by writing a C grammar, which is contained in the file CGrammar.g4.
Next we use ANTLR4 to generate a Python Lexer and Parser that parses a given input file
using the written C grammar, and constructs a CST.<br>

We implemented a Visitor, called CSTVisitor that visits all the CST nodes and transforms this into an AST.
Next we can "optimize" this AST by performing "Constant Folding" and "Constant Propagation" on this tree.
This process is performed by the ASTOptimizer visitor.
The result is an optimized AST.

We now created a symbol table data type, contained by the file SymbolTable.py.
Another visitor(CreateSymbolTableVisitor) creates this symbol table by performing another DFS of the Optimized AST.

After the table creation our errorAnalysis is called which goes over the code and outputs semantic errors.

As our final step, our AST is translated into MIPS assembler code by another visitor(AST2MIPSVisitor).

We generate 2 .dot files, one before tree optimisation and one after,
to see the full effects of "Constant folding" and "Constant propagation".

Progress:
---------
The current version of the Compiler contains all the mandatory features given in the Assignments 1 - 6.
It automatically makes use of "Constant folding" and "Constant propagation".

Additionally, it contains these optional features:
<ul>
<li> Comparison operators >=, <=, and !=.</li>
<li> Binary operator %.</li>
<li> Increment/Decrement Operations.</li>
<li> Instead of simply ignoring comments, you can increase the readability
of the generated MIPS code by retaining the comments from the input code
during the compilation process. The comments will thus be stored in the AST.
Such comments can then be put into the MIPS code.</li>
<li> Type conversion(implicit).</li>
<li> No code generated for if-clauses that are never true.</li>
</ul>

Requirements
------------
This compiler is written and can be interpreted with Python 3.10 interpreter.
The requirements and packages can be found and installed using command:

<code>pip install -r Requirements.txt</code>

Execution:
----------
To test the compiler, one can use following command:

<code>python main.py "filename"</code>

For example:

<code>python main.py test.c</code>

We made some tests that show the compilers' behavior.
The tests will create for each test file and .asm file containing the potential MIPS assembler code and
two .dot file's containing the AST's before and after optimisation.
To run our tests, the following command can be used:

<code>python video.py</code>