# Generated from CGrammar.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,184,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        4,0,42,8,0,11,0,12,0,43,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        55,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,78,8,5,1,5,1,5,5,5,82,8,5,10,5,12,
        5,85,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,96,8,6,10,6,12,
        6,99,9,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,107,8,7,10,7,12,7,110,9,7,1,
        8,1,8,1,8,1,8,1,8,1,8,5,8,118,8,8,10,8,12,8,121,9,8,1,9,1,9,1,9,
        1,9,1,9,1,9,5,9,129,8,9,10,9,12,9,132,9,9,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,3,11,144,8,11,1,12,1,12,1,12,1,12,1,
        12,3,12,151,8,12,1,13,1,13,3,13,155,8,13,1,14,1,14,1,15,1,15,1,15,
        1,15,3,15,163,8,15,1,16,1,16,1,16,3,16,168,8,16,1,17,1,17,1,18,1,
        18,3,18,174,8,18,1,19,1,19,1,19,1,19,3,19,180,8,19,1,19,1,19,1,19,
        0,5,10,12,14,16,18,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,0,7,1,0,2,6,1,0,7,8,2,0,4,4,11,12,1,0,2,3,1,0,13,18,
        1,0,19,20,2,0,29,30,32,32,186,0,41,1,0,0,0,2,54,1,0,0,0,4,56,1,0,
        0,0,6,58,1,0,0,0,8,60,1,0,0,0,10,77,1,0,0,0,12,86,1,0,0,0,14,100,
        1,0,0,0,16,111,1,0,0,0,18,122,1,0,0,0,20,133,1,0,0,0,22,143,1,0,
        0,0,24,150,1,0,0,0,26,154,1,0,0,0,28,156,1,0,0,0,30,162,1,0,0,0,
        32,167,1,0,0,0,34,169,1,0,0,0,36,173,1,0,0,0,38,175,1,0,0,0,40,42,
        3,2,1,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,
        44,45,1,0,0,0,45,46,5,0,0,1,46,1,1,0,0,0,47,48,3,26,13,0,48,49,5,
        1,0,0,49,55,1,0,0,0,50,55,3,36,18,0,51,52,3,38,19,0,52,53,5,1,0,
        0,53,55,1,0,0,0,54,47,1,0,0,0,54,50,1,0,0,0,54,51,1,0,0,0,55,3,1,
        0,0,0,56,57,7,0,0,0,57,5,1,0,0,0,58,59,7,1,0,0,59,7,1,0,0,0,60,61,
        5,9,0,0,61,62,3,26,13,0,62,63,5,10,0,0,63,9,1,0,0,0,64,65,6,5,-1,
        0,65,66,3,4,2,0,66,67,5,31,0,0,67,78,1,0,0,0,68,69,3,4,2,0,69,70,
        3,28,14,0,70,78,1,0,0,0,71,78,3,28,14,0,72,78,3,8,4,0,73,78,5,31,
        0,0,74,75,3,4,2,0,75,76,3,10,5,2,76,78,1,0,0,0,77,64,1,0,0,0,77,
        68,1,0,0,0,77,71,1,0,0,0,77,72,1,0,0,0,77,73,1,0,0,0,77,74,1,0,0,
        0,78,83,1,0,0,0,79,80,10,1,0,0,80,82,3,6,3,0,81,79,1,0,0,0,82,85,
        1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,11,1,0,0,0,85,83,1,0,0,0,
        86,87,6,6,-1,0,87,88,3,10,5,0,88,97,1,0,0,0,89,90,10,3,0,0,90,91,
        7,2,0,0,91,96,3,10,5,0,92,93,10,2,0,0,93,94,5,12,0,0,94,96,3,10,
        5,0,95,89,1,0,0,0,95,92,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,
        1,0,0,0,98,13,1,0,0,0,99,97,1,0,0,0,100,101,6,7,-1,0,101,102,3,12,
        6,0,102,108,1,0,0,0,103,104,10,2,0,0,104,105,7,3,0,0,105,107,3,12,
        6,0,106,103,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,
        0,0,109,15,1,0,0,0,110,108,1,0,0,0,111,112,6,8,-1,0,112,113,3,14,
        7,0,113,119,1,0,0,0,114,115,10,2,0,0,115,116,7,4,0,0,116,118,3,14,
        7,0,117,114,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,
        0,0,120,17,1,0,0,0,121,119,1,0,0,0,122,123,6,9,-1,0,123,124,3,16,
        8,0,124,130,1,0,0,0,125,126,10,2,0,0,126,127,7,5,0,0,127,129,3,16,
        8,0,128,125,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,
        0,0,131,19,1,0,0,0,132,130,1,0,0,0,133,134,3,18,9,0,134,21,1,0,0,
        0,135,136,3,30,15,0,136,137,5,4,0,0,137,138,5,31,0,0,138,144,1,0,
        0,0,139,140,3,30,15,0,140,141,5,31,0,0,141,144,1,0,0,0,142,144,5,
        31,0,0,143,135,1,0,0,0,143,139,1,0,0,0,143,142,1,0,0,0,144,23,1,
        0,0,0,145,146,3,22,11,0,146,147,5,21,0,0,147,148,3,20,10,0,148,151,
        1,0,0,0,149,151,3,22,11,0,150,145,1,0,0,0,150,149,1,0,0,0,151,25,
        1,0,0,0,152,155,3,20,10,0,153,155,3,24,12,0,154,152,1,0,0,0,154,
        153,1,0,0,0,155,27,1,0,0,0,156,157,7,6,0,0,157,29,1,0,0,0,158,159,
        3,34,17,0,159,160,3,32,16,0,160,163,1,0,0,0,161,163,3,32,16,0,162,
        158,1,0,0,0,162,161,1,0,0,0,163,31,1,0,0,0,164,168,5,22,0,0,165,
        168,5,23,0,0,166,168,5,24,0,0,167,164,1,0,0,0,167,165,1,0,0,0,167,
        166,1,0,0,0,168,33,1,0,0,0,169,170,5,25,0,0,170,35,1,0,0,0,171,174,
        5,27,0,0,172,174,5,28,0,0,173,171,1,0,0,0,173,172,1,0,0,0,174,37,
        1,0,0,0,175,176,5,26,0,0,176,179,5,9,0,0,177,180,5,31,0,0,178,180,
        3,28,14,0,179,177,1,0,0,0,179,178,1,0,0,0,180,181,1,0,0,0,181,182,
        5,10,0,0,182,39,1,0,0,0,16,43,54,77,83,95,97,108,119,130,143,150,
        154,162,167,173,179
    ]

class CGrammarParser ( Parser ):

    grammarFileName = "CGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'+'", "'-'", "'*'", "'&'", "'!'", 
                     "'++'", "'--'", "'('", "')'", "'/'", "'%'", "'<'", 
                     "'>'", "'=='", "'<='", "'>='", "'!='", "'&&'", "'||'", 
                     "'='", "'int'", "'float'", "'char'", "'const'", "'printf'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BLOCKCOMMENT", 
                      "SINGLE_LINE_COMMMENT", "INT", "FLOAT", "IDENTIFIER", 
                      "CHAR", "WS" ]

    RULE_prog = 0
    RULE_instr = 1
    RULE_unary_operator = 2
    RULE_post_unary_operator = 3
    RULE_parenthesis_expression = 4
    RULE_unary_expression = 5
    RULE_mul_div_expression = 6
    RULE_add_sub_expression = 7
    RULE_relational_expression = 8
    RULE_logical_expression = 9
    RULE_assignment_expression = 10
    RULE_declaration_specification = 11
    RULE_declaration = 12
    RULE_expr = 13
    RULE_constant = 14
    RULE_type = 15
    RULE_type_specifier = 16
    RULE_reserved_word = 17
    RULE_comment = 18
    RULE_printf = 19

    ruleNames =  [ "prog", "instr", "unary_operator", "post_unary_operator", 
                   "parenthesis_expression", "unary_expression", "mul_div_expression", 
                   "add_sub_expression", "relational_expression", "logical_expression", 
                   "assignment_expression", "declaration_specification", 
                   "declaration", "expr", "constant", "type", "type_specifier", 
                   "reserved_word", "comment", "printf" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    BLOCKCOMMENT=27
    SINGLE_LINE_COMMMENT=28
    INT=29
    FLOAT=30
    IDENTIFIER=31
    CHAR=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CGrammarParser.EOF, 0)

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CGrammarParser.InstrContext)
            else:
                return self.getTypedRuleContext(CGrammarParser.InstrContext,i)


        def getRuleIndex(self):
            return CGrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.instr()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8585740924) != 0)):
                    break

            self.state = 45
            self.match(CGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CGrammarParser.ExprContext,0)


        def comment(self):
            return self.getTypedRuleContext(CGrammarParser.CommentContext,0)


        def printf(self):
            return self.getTypedRuleContext(CGrammarParser.PrintfContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstr" ):
                listener.enterInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstr" ):
                listener.exitInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr" ):
                return visitor.visitInstr(self)
            else:
                return visitor.visitChildren(self)




    def instr(self):

        localctx = CGrammarParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instr)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 6, 9, 22, 23, 24, 25, 29, 30, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.expr()
                self.state = 48
                self.match(CGrammarParser.T__0)
                pass
            elif token in [27, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.comment()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.printf()
                self.state = 52
                self.match(CGrammarParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CGrammarParser.RULE_unary_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_operator" ):
                listener.enterUnary_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_operator" ):
                listener.exitUnary_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_operator" ):
                return visitor.visitUnary_operator(self)
            else:
                return visitor.visitChildren(self)




    def unary_operator(self):

        localctx = CGrammarParser.Unary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_unary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Post_unary_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CGrammarParser.RULE_post_unary_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPost_unary_operator" ):
                listener.enterPost_unary_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPost_unary_operator" ):
                listener.exitPost_unary_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPost_unary_operator" ):
                return visitor.visitPost_unary_operator(self)
            else:
                return visitor.visitChildren(self)




    def post_unary_operator(self):

        localctx = CGrammarParser.Post_unary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_post_unary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parenthesis_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_parenthesis_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis_expression" ):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis_expression" ):
                listener.exitParenthesis_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis_expression" ):
                return visitor.visitParenthesis_expression(self)
            else:
                return visitor.visitChildren(self)




    def parenthesis_expression(self):

        localctx = CGrammarParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(CGrammarParser.T__8)
            self.state = 61
            self.expr()
            self.state = 62
            self.match(CGrammarParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.iden = None # Token

        def unary_operator(self):
            return self.getTypedRuleContext(CGrammarParser.Unary_operatorContext,0)


        def IDENTIFIER(self):
            return self.getToken(CGrammarParser.IDENTIFIER, 0)

        def constant(self):
            return self.getTypedRuleContext(CGrammarParser.ConstantContext,0)


        def parenthesis_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Parenthesis_expressionContext,0)


        def unary_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Unary_expressionContext,0)


        def post_unary_operator(self):
            return self.getTypedRuleContext(CGrammarParser.Post_unary_operatorContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_unary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expression" ):
                listener.enterUnary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expression" ):
                listener.exitUnary_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expression" ):
                return visitor.visitUnary_expression(self)
            else:
                return visitor.visitChildren(self)



    def unary_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CGrammarParser.Unary_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_unary_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 65
                self.unary_operator()
                self.state = 66
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 68
                self.unary_operator()
                self.state = 69
                self.constant()
                pass

            elif la_ == 3:
                self.state = 71
                self.constant()
                pass

            elif la_ == 4:
                self.state = 72
                self.parenthesis_expression()
                pass

            elif la_ == 5:
                self.state = 73
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.state = 74
                self.unary_operator()
                self.state = 75
                self.unary_expression(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Unary_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unary_expression)
                    self.state = 79
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 80
                    self.post_unary_operator() 
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_div_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def unary_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Unary_expressionContext,0)


        def mul_div_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Mul_div_expressionContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_mul_div_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_div_expression" ):
                listener.enterMul_div_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_div_expression" ):
                listener.exitMul_div_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_div_expression" ):
                return visitor.visitMul_div_expression(self)
            else:
                return visitor.visitChildren(self)



    def mul_div_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CGrammarParser.Mul_div_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_mul_div_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.unary_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 95
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 89
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 90
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6160) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 91
                        self.unary_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 92
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 93
                        self.match(CGrammarParser.T__11)
                        self.state = 94
                        self.unary_expression(0)
                        pass

             
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_sub_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def mul_div_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Mul_div_expressionContext,0)


        def add_sub_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Add_sub_expressionContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_add_sub_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_sub_expression" ):
                listener.enterAdd_sub_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_sub_expression" ):
                listener.exitAdd_sub_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_sub_expression" ):
                return visitor.visitAdd_sub_expression(self)
            else:
                return visitor.visitChildren(self)



    def add_sub_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CGrammarParser.Add_sub_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_add_sub_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.mul_div_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Add_sub_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expression)
                    self.state = 103
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 104
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==2 or _la==3):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 105
                    self.mul_div_expression(0) 
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Relational_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def add_sub_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Add_sub_expressionContext,0)


        def relational_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Relational_expressionContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_relational_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_expression" ):
                listener.enterRelational_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_expression" ):
                listener.exitRelational_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expression" ):
                return visitor.visitRelational_expression(self)
            else:
                return visitor.visitChildren(self)



    def relational_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CGrammarParser.Relational_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_relational_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.add_sub_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Relational_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
                    self.state = 114
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 115
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 116
                    self.add_sub_expression(0) 
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def relational_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Relational_expressionContext,0)


        def logical_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Logical_expressionContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_logical_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_expression" ):
                listener.enterLogical_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_expression" ):
                listener.exitLogical_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expression" ):
                return visitor.visitLogical_expression(self)
            else:
                return visitor.visitChildren(self)



    def logical_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CGrammarParser.Logical_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_logical_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.relational_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 125
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 126
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==20):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 127
                    self.relational_expression(0) 
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assignment_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Logical_expressionContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_assignment_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_expression" ):
                listener.enterAssignment_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_expression" ):
                listener.exitAssignment_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_expression" ):
                return visitor.visitAssignment_expression(self)
            else:
                return visitor.visitChildren(self)




    def assignment_expression(self):

        localctx = CGrammarParser.Assignment_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.logical_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_specificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pointer = None # Token
            self.var = None # Token

        def type_(self):
            return self.getTypedRuleContext(CGrammarParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(CGrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CGrammarParser.RULE_declaration_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration_specification" ):
                listener.enterDeclaration_specification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration_specification" ):
                listener.exitDeclaration_specification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_specification" ):
                return visitor.visitDeclaration_specification(self)
            else:
                return visitor.visitChildren(self)




    def declaration_specification(self):

        localctx = CGrammarParser.Declaration_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_declaration_specification)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.type_()
                self.state = 136
                localctx.pointer = self.match(CGrammarParser.T__3)
                self.state = 137
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.type_()
                self.state = 140
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lvalue = None # Declaration_specificationContext
            self.assign = None # Token
            self.rvalue = None # Assignment_expressionContext

        def declaration_specification(self):
            return self.getTypedRuleContext(CGrammarParser.Declaration_specificationContext,0)


        def assignment_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Assignment_expressionContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = CGrammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declaration)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                localctx.lvalue = self.declaration_specification()
                self.state = 146
                localctx.assign = self.match(CGrammarParser.T__20)
                self.state = 147
                localctx.rvalue = self.assignment_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                localctx.lvalue = self.declaration_specification()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Assignment_expressionContext,0)


        def declaration(self):
            return self.getTypedRuleContext(CGrammarParser.DeclarationContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.assignment_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CGrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CGrammarParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(CGrammarParser.CHAR, 0)

        def getRuleIndex(self):
            return CGrammarParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = CGrammarParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 5905580032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reserved_word(self):
            return self.getTypedRuleContext(CGrammarParser.Reserved_wordContext,0)


        def type_specifier(self):
            return self.getTypedRuleContext(CGrammarParser.Type_specifierContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = CGrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_type)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.reserved_word()
                self.state = 159
                self.type_specifier()
                pass
            elif token in [22, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.type_specifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # Token


        def getRuleIndex(self):
            return CGrammarParser.RULE_type_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_specifier" ):
                listener.enterType_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_specifier" ):
                listener.exitType_specifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_specifier" ):
                return visitor.visitType_specifier(self)
            else:
                return visitor.visitChildren(self)




    def type_specifier(self):

        localctx = CGrammarParser.Type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_type_specifier)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                localctx.typ = self.match(CGrammarParser.T__21)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                localctx.typ = self.match(CGrammarParser.T__22)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                localctx.typ = self.match(CGrammarParser.T__23)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Reserved_wordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CGrammarParser.RULE_reserved_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReserved_word" ):
                listener.enterReserved_word(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReserved_word" ):
                listener.exitReserved_word(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReserved_word" ):
                return visitor.visitReserved_word(self)
            else:
                return visitor.visitChildren(self)




    def reserved_word(self):

        localctx = CGrammarParser.Reserved_wordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_reserved_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(CGrammarParser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.block = None # Token
            self.sl = None # Token

        def BLOCKCOMMENT(self):
            return self.getToken(CGrammarParser.BLOCKCOMMENT, 0)

        def SINGLE_LINE_COMMMENT(self):
            return self.getToken(CGrammarParser.SINGLE_LINE_COMMMENT, 0)

        def getRuleIndex(self):
            return CGrammarParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = CGrammarParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comment)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                localctx.block = self.match(CGrammarParser.BLOCKCOMMENT)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                localctx.sl = self.match(CGrammarParser.SINGLE_LINE_COMMMENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CGrammarParser.IDENTIFIER, 0)

        def constant(self):
            return self.getTypedRuleContext(CGrammarParser.ConstantContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_printf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintf" ):
                listener.enterPrintf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintf" ):
                listener.exitPrintf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintf" ):
                return visitor.visitPrintf(self)
            else:
                return visitor.visitChildren(self)




    def printf(self):

        localctx = CGrammarParser.PrintfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(CGrammarParser.T__25)
            self.state = 176
            self.match(CGrammarParser.T__8)
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 177
                self.match(CGrammarParser.IDENTIFIER)
                pass
            elif token in [29, 30, 32]:
                self.state = 178
                self.constant()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 181
            self.match(CGrammarParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.unary_expression_sempred
        self._predicates[6] = self.mul_div_expression_sempred
        self._predicates[7] = self.add_sub_expression_sempred
        self._predicates[8] = self.relational_expression_sempred
        self._predicates[9] = self.logical_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def unary_expression_sempred(self, localctx:Unary_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def mul_div_expression_sempred(self, localctx:Mul_div_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def add_sub_expression_sempred(self, localctx:Add_sub_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def relational_expression_sempred(self, localctx:Relational_expressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




