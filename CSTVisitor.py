import ast
import re
from CGrammarVisitor import CGrammarVisitor
from CGrammarParser import CGrammarParser
from AST import *

class CSTVisitor(CGrammarVisitor):

    def __init__(self, tree):
        self.tree = tree
        self.stack = []
        #print("Visiting the program")

    def visitProg(self, ctx):
        print("Prog")
        self.tree.Name = "Prog" + str(ctx.getRuleIndex())
        prog = ASTNode("Prog")
        for child in ctx.children:
            node = self.visit(child)
            if isinstance(node, ASTNode):
                #print("Printing:")
                prog.adopt(node)
        self.tree.setRoot(prog)


    def visitInstr(self, ctx):
        print("Inst")
        instr = ASTNode("Inst")
        if ctx.stdio:
            print(ctx.stdio.text)
        for child in ctx.children:
            node = self.visit(child)
            if isinstance(node, ASTNode):
                instr.adopt(node)
        return instr

    # Visit a parse tree produced by CGrammarParser#unary_operator.
    def visitUnary_operator(self, ctx: CGrammarParser.Unary_operatorContext):
        #print("UnaryOperator")
        op = UnaryOperator(ctx.getText())
        return op

    # Visit a parse tree produced by CGrammarParser#unary_operator.
    def visitPost_unary_operator(self, ctx: CGrammarParser.Unary_operatorContext):
        #print("PostUnaryOperator")
        op = UnaryOperator(ctx.getText())
        return op

    def visitFunction_call(self, ctx: CGrammarParser.Function_callContext):
        print("Call")
        node = Call(ctx.iden.text+"()")
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
                    newnode.value = node.value
                elif node is None:
                    newvar = ASTNode(ctx.iden.text)
                    newnode.adopt(newvar)
                else:
                    newnode.adopt(node)
            return newnode
        else:
            if ctx.iden:
                var = Variable(ctx.getText())
                return var
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CGrammarParser#mul_div_expression.
    def visitMul_div_expression(self, ctx: CGrammarParser.Mul_div_expressionContext):
        #print("MulDivExpression")
        if ctx.getChildCount() > 1:
            binOp = BinaryOperation(ctx.op.text)
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
            assign.rvalue = self.visit(ctx.rvalue)
            assign.lvalue = self.visit(ctx.lvalue)
            assign.adopt(assign.lvalue)
            assign.adopt(assign.rvalue)
            return assign
        return self.visitChildren(ctx)

    def visitDeclaration_specification(self, ctx:CGrammarParser.Declaration_specificationContext):
        print("DeclarationSpecifier")
        decl = Declaration("VariableDeclartion")
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
                            # print("Doetem dees wel?")
                            decl.adopt(child2)
                            if ctx.ptr:
                                # We are in pointer decl/def
                                decl.type = child2.value + "*"
                            else:
                                decl.type = child2.value
                elif child is ctx.ptr:
                    pointer = ASTNode("*")
                    decl.adopt(pointer)
                else:
                    var = ASTNode(ctx.var.text)
                    decl.adopt(var)
                    decl.var = var.value
        else:
            # We are just in var assignment/definition
            if ctx.ptr:
                op = UnaryOperation(self.visit(ctx.ptr).value)
                var = ASTNode(ctx.var.text)
                op.adopt(var)
                return op
            else:
                for child in ctx.children:
                    node = self.visit(child)
                    var = Variable(ctx.var.text)
                    return var
        # We return decl if we have a declaration
        return decl

    def visitDeclaration(self, ctx:CGrammarParser.DeclarationContext):
        print("Declaration")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CGrammarParser#expr.
    def visitExpr(self, ctx: CGrammarParser.ExprContext):
        print("Expr")
        for child in ctx.children:
            if not child.getText() == ";":
                node = self.visit(child)
                if isinstance(node, ASTNode):
                    return node
        return node

    # Visit a parse tree produced by CGrammarParser#conditional_statement.
    def visitConditional_statement(self, ctx:CGrammarParser.Conditional_statementContext):
        print("Conditional")
        node = Conditional("Conditional")
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
        print("Looping expressions")
        loop = ExprLoop("Loop Expr")
        if ctx.children:
            for child in ctx.children:
                node = self.visit(child)
                loop.adopt(node)
            return loop
        else:
            return None

    # Visit a parse tree produced by CGrammarParser#loops.
    def visitLoops(self, ctx:CGrammarParser.LoopsContext):
        print("Loop")
        match ctx.loop.text:
            case "while":
                print("This is a while-loop")
                node = While("Loop")
                condition = self.visit(ctx.condition)
                node.condition = condition
                #node.adopt(condition)
                body = self.visit(ctx.body)
                #scope = Scope("While-Scope")
                #scope.children = body.children
                node.body = body
                #node.adopt(scope)
            case "for":
                print("This is a for-loop")
                node = While("Loop")
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
        print("Jumps")
        match ctx.jump.text:
            case "break":
                print("This is a break")
                node = Jump("break")
                return node
            case "continue":
                print("This is a continue")
                node = Jump("continue")
                return node
            case "return":
                print("This is a return")
                node = Jump("return")
                if ctx.beforereturn:
                    beforereturn = self.visit(ctx.beforereturn)
                    node.adopt(beforereturn)
                return node
            case _:
                print("Not implemented")
        return None

    # Visit a parse tree produced by CGrammarParser#scope.
    def visitScope(self, ctx:CGrammarParser.ScopeContext):
        print("Scope")
        node = Scope("UnnamedScope")
        for child in ctx.children:
            if not child.getText() == "{" and not child.getText() == "}":
                childnode = self.visit(child)
                node.adopt(childnode)
        return node

    def visitParameterlist(self, ctx:CGrammarParser.ParameterlistContext):
        print("Parameters")
        params = ASTNode("Params")
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
        print("Arguments")
        args = ASTNode("Arguments")
        if ctx.ass:
            ass = self.visit(ctx.ass)
            args.adopt(ass)
        if ctx.args:
            param = self.visit(ctx.args)
            if isinstance(param, ASTNode):
                for child in param.children:
                    args.adopt(child)
        return args
    def visitFunction(self, ctx:CGrammarParser.FunctionContext):
        print("Function declaration/definition")
        returntype = self.visit(ctx.returntype)
        print("Return type:")
        print(returntype.value)
        print("Function name:")
        funcname = ctx.funcname.text
        print(funcname)
        function = Function(str(funcname))
        function.returnType = returntype
        if ctx.param:
            print("Function param:")
            params = self.visit(ctx.param)
            function.params = params.children
            for child in function.params:
                print(child.type)

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
        return const

    # Visit a parse tree produced by CGrammarParser#type.
    def visitType(self, ctx:CGrammarParser.TypeContext):
        #print("Type")
        type = Variable("Variable")
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
        type.type = "type"
        #print("EndOfTypeSpecifier")
        return type

    # Visit a parse tree produced by CGrammarParser#reserved_word.
    def visitReserved_word(self, ctx:CGrammarParser.Reserved_wordContext):
        #print("ReservedWord")
        word = ASTNode(ctx.getText())
        word.type = "reserved_word"
        return word

    # Visit a parse tree produced by CGrammarParser#reserved_word.
    def visitPointer(self, ctx:CGrammarParser.Reserved_wordContext):
        #print("Pointer")
        word = ASTNode(ctx.getText())
        word.type = "pointer"
        return word

    # Visit a parse tree produced by CGrammarParser#reserved_word.
    def visitComment(self, ctx: CGrammarParser.CommentContext):
        #print("Comment--------------------------")
        if ctx.block:
            comment = MLComment(ctx.block.text)
        elif ctx.sl:
            comment = SLComment(ctx.sl.text)
        return comment

    def visitPrintf(self, ctx: CGrammarParser.PrintfContext):
        print("Printf")
        result = re.search('\((.+?)\)', ctx.getText()).group(1)
        #print("need this")
        #print(result)
        node = ASTNode(result)
        printf = PrintF("printf()")
        printf.adopt(node)
        return printf
