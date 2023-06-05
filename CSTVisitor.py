import ast
import re
from CGrammarVisitor import CGrammarVisitor
from CGrammarParser import CGrammarParser
from AST import *

class CSTVisitor(CGrammarVisitor):

    deref = False

    def __init__(self, tree):
        self.tree = tree
        self.stack = []
        self.deref = False
        #print("Visiting the program")

    def visitProg(self, ctx):
        #print("Prog")
        self.tree.Name = "Prog" + str(ctx.getRuleIndex())
        prog = ASTNode("Prog")
        start = ctx.start
        prog.line = start.line
        prog.column = start.column
        for child in ctx.children:
            node = self.visit(child)
            if isinstance(node, ASTNode):
                #print("Printing:")
                prog.adopt(node)
        self.tree.setRoot(prog)


    def visitInstr(self, ctx):
        #print("Inst")
        instr = ASTNode("Inst")
        start = ctx.start
        instr.line = start.line
        instr.column = start.column
        if ctx.stdio:
            #print(ctx.stdio.text)
            instr = Include("Inst")
            start = ctx.start
            instr.line = start.line
            instr.column = start.column
            instr.value = ctx.stdio.text
            instr.name = ctx.stdio.text
            return instr
        for child in ctx.children:
            node = self.visit(child)
            if isinstance(node, ASTNode):
                instr.adopt(node)
        return instr

    # Visit a parse tree produced by CGrammarParser#unary_operator.
    def visitUnary_operator(self, ctx: CGrammarParser.Unary_operatorContext):
        #print("UnaryOperator")
        op = UnaryOperator(ctx.getText())
        start = ctx.start
        op.line = start.line
        op.column = start.column
        return op

    # Visit a parse tree produced by CGrammarParser#unary_operator.
    def visitPost_unary_operator(self, ctx: CGrammarParser.Unary_operatorContext):
        #print("PostUnaryOperator")
        if ctx.ass:
            #op = UnaryOperator("[]")
            array = ArrayVariable("[]")
            start = ctx.start
            array.line = start.line
            array.column = start.column
            node = self.visit(ctx.ass)
            array.adopt(node)
            return array
            #op.adopt(node)
        else:
            op = UnaryOperator(ctx.getText())
        return op

    def visitFunction_call(self, ctx: CGrammarParser.Function_callContext):
        #print("Call")
        node = Call(ctx.iden.text+"()")
        start = ctx.start
        node.line = start.line
        node.column = start.column
        if ctx.args:
            children = self.visit(ctx.args)
            node.children = children.children
        return node


    # Visit a parse tree produced by CGrammarParser#parenthesis_expression.
    def visitParenthesis_expression(self, ctx: CGrammarParser.Parenthesis_expressionContext):
        #print("ParenthesisExpression")
        if len(ctx.children) == 3:
            for child in ctx.children:
                if not child.getText() == '(' and not child.getText() == ')':
                    #print("No parenthesis")
                    node = self.visit(child)
                    return node
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#unary_expression.
    def visitUnary_expression(self, ctx: CGrammarParser.Unary_expressionContext):
        #print("UnaryExpression")
        if ctx.call:
            node = self.visit(ctx.call)
            return node
        elif len(ctx.children) == 2:
            newnode = UnaryOperation("")
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, UnaryOperator):
                    #print("DEEEEEEEEEEEEEESEEEEEEEEEEEEEEEEEEEEEEEEEEEEEES")
                    newnode.value = node.value
                    #print(newnode)
                elif isinstance(node, ArrayVariable):
                    #print("Tis nen array")
                    if newnode.children:
                        node.value = newnode.children[0].value
                        node.index = node.children[0]
                        node.rvalue = False
                        return node
                    else:
                        newnode.adopt(node)
                elif node is None:
                    newvar = Variable(ctx.iden.text)
                    start = ctx.start
                    newvar.line = start.line
                    newvar.column = start.column
                    newnode.adopt(newvar)
                else:
                    #print("DEEEEEEEEEEEEEES")
                    #print(newnode.value)
                    newnode.adopt(node)
            return newnode
        else:
            if ctx.iden:
                var = Variable(ctx.getText())
                start = ctx.start
                var.line = start.line
                var.column = start.column
                return var
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#mul_div_expression.
    def visitMul_div_expression(self, ctx: CGrammarParser.Mul_div_expressionContext):
        #print("MulDivExpression")
        if ctx.getChildCount() > 1:
            binOp = BinaryOperation(ctx.op.text)
            start = ctx.start
            binOp.line = start.line
            binOp.column = start.column
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    binOp.adopt(node)
            return binOp
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#add_sub_expression.
    def visitAdd_sub_expression(self, ctx: CGrammarParser.Add_sub_expressionContext):
        #print("AddSubExpression")
        if ctx.getChildCount() > 1:
            binOp = BinaryOperation(ctx.op.text)
            start = ctx.start
            binOp.line = start.line
            binOp.column = start.column
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    binOp.adopt(node)
            return binOp
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#relational_expression.
    def visitRelational_expression(self, ctx: CGrammarParser.Relational_expressionContext):
        #print("RelationalExpression")
        if ctx.getChildCount() > 1:
            relOp = BinaryOperation(ctx.op.text)
            start = ctx.start
            relOp.line = start.line
            relOp.column = start.column
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    relOp.adopt(node)
            return relOp
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#logical_expression.
    def visitLogical_expression(self, ctx: CGrammarParser.Logical_expressionContext):
        #print("LogicalExpression")
        if ctx.getChildCount() > 1:
            logOp = BinaryOperation(ctx.op.text)
            start = ctx.start
            logOp.line = start.line
            logOp.column = start.column
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    logOp.adopt(node)
            return logOp
        else:
            return self.visitChildren(ctx)

    def visitAssignment_expression(self, ctx:CGrammarParser.Assignment_expressionContext):
        if ctx.assign:
            assign = Assigment(ctx.assign.text)
            start = ctx.start
            assign.line = start.line
            assign.column = start.column
            assign.rvalue = self.visit(ctx.rvalue)
            assign.lvalue = self.visit(ctx.lvalue)
            assign.adopt(assign.lvalue)
            assign.adopt(assign.rvalue)
            return assign
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#reserved_word.
    def visitPointer(self, ctx:CGrammarParser.PointerContext):
        #print("Pointer")
        if self.deref:
            op = UnaryOperation("*")
            start = ctx.start
            op.line = start.line
            op.column = start.column
            if ctx.ptr:
                ptr = self.visit(ctx.ptr)
                op.adopt(ptr)
                return op
            else:
                return op
        pointer = Pointer("*")
        start = ctx.start
        pointer.line = start.line
        pointer.column = start.column
        if ctx.ptr:
            ptr = self.visit(ctx.ptr)
            pointer.adopt(ptr)
        return pointer

    def visitDeclaration_specification(self, ctx:CGrammarParser.Declaration_specificationContext):
        #print("DeclarationSpecifier")
        decl = Declaration("VariableDeclartion")
        start = ctx.start
        decl.line = start.line
        decl.column = start.column
        decl.attr = ""
        # Test for declaration/definition or just var assignment
        if ctx.typ:
            # We are in decl/def
            for child in ctx.children:
                node = self.visit(child)
                if isinstance(node, Variable):
                    for child2 in node.children:
                        if child2.type == "reserved_word":
                            decl.adopt(child2)
                            decl.attr = child2.value
                        if child2.type == "type":
                            #print("Doetem dees wel?")
                            decl.adopt(child2)
                            decl.type = child2.value
                elif child == ctx.ptr:
                    node = self.visit(ctx.ptr)
                    decl.adopt(node)
                    decl.pointer = node
                elif child == ctx.arr:
                    array = self.visit(ctx.arr)
                    decl.array = array
                    decl.adopt(array)
                else:
                    #print("En dees?")
                    var = ASTNode(ctx.var.text)
                    start = ctx.start
                    var.line = start.line
                    var.column = start.column
                    decl.adopt(var)
                    decl.var = var.value
        else:
            # We are just in var assignment/definition
            if ctx.ptr:
                self.deref = True
                node = self.visit(ctx.ptr)
                self.deref = False
                op = PointerDeref("PtrDereference")
                start = ctx.start
                op.line = start.line
                op.column = start.column
                op.adopt(node)
                #op = UnaryOperation(node.value)
                #op.children = node.children
                var = Variable(ctx.var.text)
                start = ctx.start
                var.line = start.line
                var.column = start.column
                #op.adopt(var)
                op.variable = var
                return op
            elif ctx.arr:
                #print("Creating array")
                index = self.visit(ctx.arr)
                node = ArrayVariable(ctx.var.text)
                start = ctx.start
                node.line = start.line
                node.column = start.column
                node.lvalue = True
                node.index = index
                return node
            else:
                for child in ctx.children:
                    node = self.visit(child)
                    var = Variable(ctx.var.text)
                    start = ctx.start
                    var.line = start.line
                    var.column = start.column
                    return var
        # We return decl if we have a declaration
        return decl
    def visitArray(self, ctx:CGrammarParser.ArrayContext):
        #print("Array")
        value = "-1"
        for child in ctx.children:
            if not child.getText() == "[" and not child.getText() == "]":
                value = self.visit(child)
        return value

    def visitDeclaration(self, ctx:CGrammarParser.DeclarationContext):
        #print("Declaration")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#expr.
    def visitExpr(self, ctx: CGrammarParser.ExprContext):
        #print("Expr")
        for child in ctx.children:
            if not child.getText() == ";":
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    return node
        return node

    # Visit a parse tree produced by CGrammarParser#conditional_statement.
    def visitConditional_statement(self, ctx:CGrammarParser.Conditional_statementContext):
        #print("Conditional")
        node = Conditional("Conditional")
        start = ctx.start
        node.line = start.line
        node.column = start.column
        condition = self.visit(ctx.condition)
        node.adopt(condition)
        node.condition = condition
        ifbody = self.visit(ctx.ifbody)
        node.ifbody = ifbody
        node.adopt(ifbody)
        if ctx.elsebody:
            elsebody = self.visit(ctx.elsebody)
            node.adopt(elsebody)
            node.elsebody = elsebody
        return node

    def visitExpr_loop(self, ctx:CGrammarParser.Expr_loopContext):
        #print("Looping expressions")
        loop = ExprLoop("Loop Expr")
        start = ctx.start
        loop.line = start.line
        loop.column = start.column
        if ctx.children:
            for child in ctx.children:
                node = self.visit(child)
                loop.adopt(node)
            return loop
        else:
            return None

    # Visit a parse tree produced by CGrammarParser#loops.
    def visitLoops(self, ctx:CGrammarParser.LoopsContext):
        #print("Loop")
        match ctx.loop.text:
            case "while":
                #print("This is a while-loop")
                node = While("Loop")
                start = ctx.start
                node.line = start.line
                node.column = start.column
                condition = self.visit(ctx.condition)
                node.condition = condition
                #node.adopt(condition)
                body = self.visit(ctx.body)
                #scope = Scope("While-Scope")
                #scope.children = body.children
                node.body = body
                #node.adopt(scope)
            case "for":
                #print("This is a for-loop")
                node = While("Loop")
                start = ctx.start
                node.line = start.line
                node.column = start.column
                condition = self.visit(ctx.condition)
                after = self.visit(ctx.after)
                before = self.visit(ctx.before)
                node.beforeLoop = before
                node.adopt(before)
                node.afterLoop = after
                node.adopt(after)
                node.condition = condition
                node.adopt(condition)
                body = self.visit(ctx.body)
                #scope = Scope("While-Scope")
                #scope.children = body.children
                node.body = body
                #node.adopt(scope)
            case _:
                print("Not implemented")
        return node

    def visitJumps(self, ctx:CGrammarParser.JumpsContext):
        #print("Jumps")
        match ctx.jump.text:
            case "break":
                #print("This is a break")
                node = Jump("break")
                start = ctx.start
                node.line = start.line
                node.column = start.column
                return node
            case "continue":
                #print("This is a continue")
                node = Jump("continue")
                start = ctx.start
                node.line = start.line
                node.column = start.column
                return node
            case "return":
                #print("This is a return")
                node = Jump("return")
                start = ctx.start
                node.line = start.line
                node.column = start.column
                if ctx.beforereturn:
                    beforereturn = self.visit(ctx.beforereturn)
                    node.adopt(beforereturn)
                return node
            case _:
                print("Not implemented")
        return None

    # Visit a parse tree produced by CGrammarParser#scope.
    def visitScope(self, ctx:CGrammarParser.ScopeContext):
        #print("Scope")
        node = Scope("UnnamedScope")
        start = ctx.start
        node.line = start.line
        node.column = start.column
        for child in ctx.children:
            if not child.getText() == "{" and not child.getText() == "}":
                childnode = self.visit(child)
                if childnode is not None:
                    node.adopt(childnode)
        return node




    def visitParameterlist(self, ctx:CGrammarParser.ParameterlistContext):
        #print("Parameters")
        params = ASTNode("Params")
        start = ctx.start
        params.line = start.line
        params.column = start.column
        if ctx.typ:
            typ = self.visit(ctx.typ)
            params.adopt(typ)
        if ctx.decl:
            decl = self.visit(ctx.decl)
            params.adopt(decl)
        if ctx.param:
            param = self.visit(ctx.param)
            if isinstance(param, ASTNode):
                print(len(param.children))
                for child in param.children:
                    params.adopt(child)
        return params

    def visitArgumentlist(self, ctx:CGrammarParser.ArgumentlistContext):
        #print("TEEEEEEEEEEEEEEEEEEEEEEEST")
        #print("Arguments")
        args = ASTNode("Arguments")
        start = ctx.start
        args.line = start.line
        args.column = start.column
        if ctx.ass:
            ass = self.visit(ctx.ass)
            args.adopt(ass)
            #print(ass.value)
        if ctx.args:
            param = self.visit(ctx.args)
            if isinstance(param, ASTNode):
                for child in param.children:
                    args.adopt(child)
        return args

    def visitPrintfArgslist(self, ctx:CGrammarParser.PrintfArgslistContext):
        #print("TEEEEEEEEEEEEEEEEEEEEEEEST")
        args = ASTNode("Arguments")
        start = ctx.start
        args.line = start.line
        args.column = start.column
        if ctx.string:
            node = String(ctx.string.text)
            #print(node.value)
            args.adopt(node)
        if ctx.ass:
            ass = self.visit(ctx.ass)
            #print(ass)
            args.adopt(ass)
            #print(ass.value)
        if ctx.args:
            param = self.visit(ctx.args)
            if isinstance(param, ASTNode):
                for child in param.children:
                    args.adopt(child)
        #print("We are returning:")
        #print(args)
        return args

    def visitFunction(self, ctx:CGrammarParser.FunctionContext):
        #print("Function declaration/definition")
        returntype = self.visit(ctx.returntype)
        #print("Return type:")
        #print(returntype.value)
        #print("Function name:")
        funcname = ctx.funcname.text
        #print(funcname)
        function = Function(str(funcname))
        start = ctx.start
        function.line = start.line
        function.column = start.column
        function.returnType = returntype
        if ctx.param:
            #print("Function param:")
            params = self.visit(ctx.param)
            function.params = params.children
            '''
            for child in function.params:
                print(child.type)
            '''

        # If it contains a body, it's no definition and only declaration
        if ctx.body:
            function.hasbody = True
            if ctx.funcbody:
                body = self.visit(ctx.funcbody)
                function.body = body

        return function


    # Visit a parse tree produced by CGrammarParser#constant.
    def visitConstant(self, ctx: CGrammarParser.ConstantContext):
        #print("Constant")
        const = Constant(ctx.getText())
        start = ctx.start
        const.line = start.line
        const.column = start.column
        return const

    # Visit a parse tree produced by CGrammarParser#type.
    def visitType(self, ctx:CGrammarParser.TypeContext):
        #print("Type")
        type = Variable("Variable")
        start = ctx.start
        type.line = start.line
        type.column = start.column
        for child in ctx.children:
            node = self.visit(child)
            if isinstance(node, ASTNode):
                type.adopt(node)
                if node.type == "type":
                    type.type = node.value
                if node.type == "reserverd_word":
                    type.attr = node.value
            else:
                type.name = str(child)
        #print("EndOfType")
        return type

    def visitType_specifier(self, ctx:CGrammarParser.Reserved_wordContext):
        #print("TypeSpecifier")
        #print("Type")
        #print(ctx.typ.text)
        type = ASTNode(ctx.typ.text)
        start = ctx.start
        type.line = start.line
        type.column = start.column
        type.type = "type"
        #print("EndOfTypeSpecifier")
        return type

    # Visit a parse tree produced by CGrammarParser#reserved_word.
    def visitReserved_word(self, ctx:CGrammarParser.Reserved_wordContext):
        #print("ReservedWord")
        word = ASTNode(ctx.getText())
        start = ctx.start
        word.line = start.line
        word.column = start.column
        word.type = "reserved_word"
        return word


    # Visit a parse tree produced by CGrammarParser#reserved_word.
    def visitComment(self, ctx: CGrammarParser.CommentContext):
        #print("Comment--------------------------")
        if ctx.block:
            comment = MLComment(ctx.block.text)
            start = ctx.start
            comment.line = start.line
            comment.column = start.column
        elif ctx.sl:
            comment = SLComment(ctx.sl.text)
            start = ctx.start
            comment.line = start.line
            comment.column = start.column
        return comment

    def visitPrintf(self, ctx: CGrammarParser.PrintfContext):
        #print("Printf")
        printf = PrintF("Printf()")
        start = ctx.start
        printf.line = start.line
        printf.column = start.column
        if ctx.form:
            form = ctx.form.text
            format = ASTNode(form)
            start = ctx.start
            format.line = start.line
            format.column = start.column
            format.value = format.value.replace("\"", "")
            printf.format = format
            #print(ctx.form.text)
        if ctx.args:
            #print("ARRRRG")
            node = self.visit(ctx.args)
            #print("We returned")
            #print(node)
            printf.args = node.children
            printf.adopt(node)
        #print("Number of args:")
        #print(len(printf.args))
        return printf

    def visitScanf(self, ctx: CGrammarParser.ScanfContext):
        #print("ScanF")
        printf = ScanF("Scanf()")
        start = ctx.start
        printf.line = start.line
        printf.column = start.column
        if ctx.form:
            form = ctx.form.text
            format = ASTNode(form)
            start = ctx.start
            format.line = start.line
            format.column = start.column
            printf.format = format
            #print(ctx.form.text)
        if ctx.args:
            node = self.visit(ctx.args)
            printf.args = node
        return printf