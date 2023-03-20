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
        4,1,31,162,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,4,0,38,8,0,11,0,12,0,
        39,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,68,8,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,79,8,5,10,5,12,5,82,9,5,1,6,1,6,
        1,6,1,6,1,6,1,6,5,6,90,8,6,10,6,12,6,93,9,6,1,7,1,7,1,7,1,7,1,7,
        1,7,5,7,101,8,7,10,7,12,7,104,9,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,112,
        8,8,10,8,12,8,115,9,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,127,8,10,1,11,1,11,1,11,1,11,1,11,3,11,134,8,11,1,12,1,
        12,3,12,138,8,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,148,
        8,14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,3,17,158,8,17,1,17,
        1,17,1,17,0,4,10,12,14,16,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,0,7,1,0,2,6,2,0,4,4,9,9,1,0,2,3,1,0,11,16,1,0,17,18,
        2,0,27,28,30,30,1,0,25,26,163,0,37,1,0,0,0,2,50,1,0,0,0,4,52,1,0,
        0,0,6,54,1,0,0,0,8,67,1,0,0,0,10,69,1,0,0,0,12,83,1,0,0,0,14,94,
        1,0,0,0,16,105,1,0,0,0,18,116,1,0,0,0,20,126,1,0,0,0,22,133,1,0,
        0,0,24,137,1,0,0,0,26,139,1,0,0,0,28,147,1,0,0,0,30,149,1,0,0,0,
        32,151,1,0,0,0,34,153,1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,39,
        1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,0,0,1,
        42,1,1,0,0,0,43,44,3,24,12,0,44,45,5,1,0,0,45,51,1,0,0,0,46,51,3,
        32,16,0,47,48,3,34,17,0,48,49,5,1,0,0,49,51,1,0,0,0,50,43,1,0,0,
        0,50,46,1,0,0,0,50,47,1,0,0,0,51,3,1,0,0,0,52,53,7,0,0,0,53,5,1,
        0,0,0,54,55,5,7,0,0,55,56,3,24,12,0,56,57,5,8,0,0,57,7,1,0,0,0,58,
        59,3,4,2,0,59,60,5,29,0,0,60,68,1,0,0,0,61,62,3,4,2,0,62,63,3,26,
        13,0,63,68,1,0,0,0,64,68,3,26,13,0,65,68,3,6,3,0,66,68,5,29,0,0,
        67,58,1,0,0,0,67,61,1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,
        0,0,0,68,9,1,0,0,0,69,70,6,5,-1,0,70,71,3,8,4,0,71,80,1,0,0,0,72,
        73,10,3,0,0,73,74,7,1,0,0,74,79,3,8,4,0,75,76,10,2,0,0,76,77,5,10,
        0,0,77,79,3,8,4,0,78,72,1,0,0,0,78,75,1,0,0,0,79,82,1,0,0,0,80,78,
        1,0,0,0,80,81,1,0,0,0,81,11,1,0,0,0,82,80,1,0,0,0,83,84,6,6,-1,0,
        84,85,3,10,5,0,85,91,1,0,0,0,86,87,10,2,0,0,87,88,7,2,0,0,88,90,
        3,10,5,0,89,86,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,
        92,13,1,0,0,0,93,91,1,0,0,0,94,95,6,7,-1,0,95,96,3,12,6,0,96,102,
        1,0,0,0,97,98,10,2,0,0,98,99,7,3,0,0,99,101,3,12,6,0,100,97,1,0,
        0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,15,1,0,0,
        0,104,102,1,0,0,0,105,106,6,8,-1,0,106,107,3,14,7,0,107,113,1,0,
        0,0,108,109,10,2,0,0,109,110,7,4,0,0,110,112,3,14,7,0,111,108,1,
        0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,17,1,0,
        0,0,115,113,1,0,0,0,116,117,3,16,8,0,117,19,1,0,0,0,118,119,3,28,
        14,0,119,120,5,4,0,0,120,121,5,29,0,0,121,127,1,0,0,0,122,123,3,
        28,14,0,123,124,5,29,0,0,124,127,1,0,0,0,125,127,5,29,0,0,126,118,
        1,0,0,0,126,122,1,0,0,0,126,125,1,0,0,0,127,21,1,0,0,0,128,129,3,
        20,10,0,129,130,5,19,0,0,130,131,3,18,9,0,131,134,1,0,0,0,132,134,
        3,20,10,0,133,128,1,0,0,0,133,132,1,0,0,0,134,23,1,0,0,0,135,138,
        3,18,9,0,136,138,3,22,11,0,137,135,1,0,0,0,137,136,1,0,0,0,138,25,
        1,0,0,0,139,140,7,5,0,0,140,27,1,0,0,0,141,142,3,30,15,0,142,143,
        3,28,14,0,143,148,1,0,0,0,144,148,5,20,0,0,145,148,5,21,0,0,146,
        148,5,22,0,0,147,141,1,0,0,0,147,144,1,0,0,0,147,145,1,0,0,0,147,
        146,1,0,0,0,148,29,1,0,0,0,149,150,5,23,0,0,150,31,1,0,0,0,151,152,
        7,6,0,0,152,33,1,0,0,0,153,154,5,24,0,0,154,157,5,7,0,0,155,158,
        5,29,0,0,156,158,3,26,13,0,157,155,1,0,0,0,157,156,1,0,0,0,158,159,
        1,0,0,0,159,160,5,8,0,0,160,35,1,0,0,0,13,39,50,67,78,80,91,102,
        113,126,133,137,147,157
    ]

class CGrammarParser ( Parser ):

    grammarFileName = "CGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'+'", "'-'", "'*'", "'&'", "'!'", 
                     "'('", "')'", "'/'", "'%'", "'<'", "'>'", "'=='", "'<='", 
                     "'>='", "'!='", "'&&'", "'||'", "'='", "'int'", "'float'", 
                     "'char'", "'const'", "'printf'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BLOCKCOMMENT", "SINGLE_LINE_COMMMENT", 
                      "INT", "FLOAT", "IDENTIFIER", "CHAR", "WS" ]

    RULE_prog = 0
    RULE_instr = 1
    RULE_unary_operator = 2
    RULE_parenthesis_expression = 3
    RULE_unary_expression = 4
    RULE_mul_div_expression = 5
    RULE_add_sub_expression = 6
    RULE_relational_expression = 7
    RULE_logical_expression = 8
    RULE_assignment_expression = 9
    RULE_declaration_specification = 10
    RULE_declaration = 11
    RULE_expr = 12
    RULE_constant = 13
    RULE_type = 14
    RULE_reserved_word = 15
    RULE_comment = 16
    RULE_printf = 17

    ruleNames =  [ "prog", "instr", "unary_operator", "parenthesis_expression", 
                   "unary_expression", "mul_div_expression", "add_sub_expression", 
                   "relational_expression", "logical_expression", "assignment_expression", 
                   "declaration_specification", "declaration", "expr", "constant", 
                   "type", "reserved_word", "comment", "printf" ]

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
    BLOCKCOMMENT=25
    SINGLE_LINE_COMMMENT=26
    INT=27
    FLOAT=28
    IDENTIFIER=29
    CHAR=30
    WS=31

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
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.instr()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2146435324) != 0)):
                    break

            self.state = 41
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
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 6, 7, 20, 21, 22, 23, 27, 28, 29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.expr()
                self.state = 44
                self.match(CGrammarParser.T__0)
                pass
            elif token in [25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.comment()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.printf()
                self.state = 48
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
            self.state = 52
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
        self.enterRule(localctx, 6, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(CGrammarParser.T__6)
            self.state = 55
            self.expr()
            self.state = 56
            self.match(CGrammarParser.T__7)
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




    def unary_expression(self):

        localctx = CGrammarParser.Unary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unary_expression)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.unary_operator()
                self.state = 59
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.unary_operator()
                self.state = 62
                self.constant()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.parenthesis_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_mul_div_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.unary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 78
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 72
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 73
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        self.unary_expression()
                        pass

                    elif la_ == 2:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 75
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 76
                        self.match(CGrammarParser.T__9)
                        self.state = 77
                        self.unary_expression()
                        pass

             
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_add_sub_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.mul_div_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Add_sub_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expression)
                    self.state = 86
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 87
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==2 or _la==3):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 88
                    self.mul_div_expression(0) 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_relational_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.add_sub_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Relational_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
                    self.state = 97
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 98
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 99
                    self.add_sub_expression(0) 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_logical_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.relational_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 108
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 109
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==18):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 110
                    self.relational_expression(0) 
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_assignment_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
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
        self.enterRule(localctx, 20, self.RULE_declaration_specification)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.type_()
                self.state = 119
                self.match(CGrammarParser.T__3)
                self.state = 120
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.type_()
                self.state = 123
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
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
            self.assign = None # Token

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
        self.enterRule(localctx, 22, self.RULE_declaration)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.declaration_specification()
                self.state = 129
                localctx.assign = self.match(CGrammarParser.T__18)
                self.state = 130
                self.assignment_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.declaration_specification()
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
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.assignment_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
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
        self.enterRule(localctx, 26, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1476395008) != 0)):
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


        def type_(self):
            return self.getTypedRuleContext(CGrammarParser.TypeContext,0)


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
        self.enterRule(localctx, 28, self.RULE_type)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.reserved_word()
                self.state = 142
                self.type_()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(CGrammarParser.T__19)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.match(CGrammarParser.T__20)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.match(CGrammarParser.T__21)
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
        self.enterRule(localctx, 30, self.RULE_reserved_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(CGrammarParser.T__22)
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
        self.enterRule(localctx, 32, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not(_la==25 or _la==26):
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
        self.enterRule(localctx, 34, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(CGrammarParser.T__23)
            self.state = 154
            self.match(CGrammarParser.T__6)
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.state = 155
                self.match(CGrammarParser.IDENTIFIER)
                pass
            elif token in [27, 28, 30]:
                self.state = 156
                self.constant()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 159
            self.match(CGrammarParser.T__7)
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
        self._predicates[5] = self.mul_div_expression_sempred
        self._predicates[6] = self.add_sub_expression_sempred
        self._predicates[7] = self.relational_expression_sempred
        self._predicates[8] = self.logical_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def mul_div_expression_sempred(self, localctx:Mul_div_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def add_sub_expression_sempred(self, localctx:Add_sub_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def relational_expression_sempred(self, localctx:Relational_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




