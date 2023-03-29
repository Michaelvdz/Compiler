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
        4,1,31,172,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,4,0,40,8,0,
        11,0,12,0,41,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,
        1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,73,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,84,8,5,10,
        5,12,5,87,9,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,95,8,6,10,6,12,6,98,9,
        6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,106,8,7,10,7,12,7,109,9,7,1,8,1,8,
        1,8,1,8,1,8,1,8,5,8,117,8,8,10,8,12,8,120,9,8,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,132,8,10,1,11,1,11,1,11,1,11,
        1,11,3,11,139,8,11,1,12,1,12,3,12,143,8,12,1,13,1,13,1,14,1,14,1,
        14,1,14,3,14,151,8,14,1,15,1,15,1,15,3,15,156,8,15,1,16,1,16,1,17,
        1,17,3,17,162,8,17,1,18,1,18,1,18,1,18,3,18,168,8,18,1,18,1,18,1,
        18,0,4,10,12,14,16,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,0,6,1,0,2,6,2,0,4,4,9,9,1,0,2,3,1,0,11,16,1,0,17,18,2,0,
        27,28,30,30,174,0,39,1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,0,6,56,1,0,
        0,0,8,72,1,0,0,0,10,74,1,0,0,0,12,88,1,0,0,0,14,99,1,0,0,0,16,110,
        1,0,0,0,18,121,1,0,0,0,20,131,1,0,0,0,22,138,1,0,0,0,24,142,1,0,
        0,0,26,144,1,0,0,0,28,150,1,0,0,0,30,155,1,0,0,0,32,157,1,0,0,0,
        34,161,1,0,0,0,36,163,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,41,
        1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,5,0,0,1,
        44,1,1,0,0,0,45,46,3,24,12,0,46,47,5,1,0,0,47,53,1,0,0,0,48,53,3,
        34,17,0,49,50,3,36,18,0,50,51,5,1,0,0,51,53,1,0,0,0,52,45,1,0,0,
        0,52,48,1,0,0,0,52,49,1,0,0,0,53,3,1,0,0,0,54,55,7,0,0,0,55,5,1,
        0,0,0,56,57,5,7,0,0,57,58,3,24,12,0,58,59,5,8,0,0,59,7,1,0,0,0,60,
        61,3,4,2,0,61,62,5,29,0,0,62,73,1,0,0,0,63,64,3,4,2,0,64,65,3,26,
        13,0,65,73,1,0,0,0,66,73,3,26,13,0,67,73,3,6,3,0,68,73,5,29,0,0,
        69,70,3,4,2,0,70,71,3,8,4,0,71,73,1,0,0,0,72,60,1,0,0,0,72,63,1,
        0,0,0,72,66,1,0,0,0,72,67,1,0,0,0,72,68,1,0,0,0,72,69,1,0,0,0,73,
        9,1,0,0,0,74,75,6,5,-1,0,75,76,3,8,4,0,76,85,1,0,0,0,77,78,10,3,
        0,0,78,79,7,1,0,0,79,84,3,8,4,0,80,81,10,2,0,0,81,82,5,10,0,0,82,
        84,3,8,4,0,83,77,1,0,0,0,83,80,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,
        0,85,86,1,0,0,0,86,11,1,0,0,0,87,85,1,0,0,0,88,89,6,6,-1,0,89,90,
        3,10,5,0,90,96,1,0,0,0,91,92,10,2,0,0,92,93,7,2,0,0,93,95,3,10,5,
        0,94,91,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,13,
        1,0,0,0,98,96,1,0,0,0,99,100,6,7,-1,0,100,101,3,12,6,0,101,107,1,
        0,0,0,102,103,10,2,0,0,103,104,7,3,0,0,104,106,3,12,6,0,105,102,
        1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,15,1,
        0,0,0,109,107,1,0,0,0,110,111,6,8,-1,0,111,112,3,14,7,0,112,118,
        1,0,0,0,113,114,10,2,0,0,114,115,7,4,0,0,115,117,3,14,7,0,116,113,
        1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,17,1,
        0,0,0,120,118,1,0,0,0,121,122,3,16,8,0,122,19,1,0,0,0,123,124,3,
        28,14,0,124,125,5,4,0,0,125,126,5,29,0,0,126,132,1,0,0,0,127,128,
        3,28,14,0,128,129,5,29,0,0,129,132,1,0,0,0,130,132,5,29,0,0,131,
        123,1,0,0,0,131,127,1,0,0,0,131,130,1,0,0,0,132,21,1,0,0,0,133,134,
        3,20,10,0,134,135,5,19,0,0,135,136,3,18,9,0,136,139,1,0,0,0,137,
        139,3,20,10,0,138,133,1,0,0,0,138,137,1,0,0,0,139,23,1,0,0,0,140,
        143,3,18,9,0,141,143,3,22,11,0,142,140,1,0,0,0,142,141,1,0,0,0,143,
        25,1,0,0,0,144,145,7,5,0,0,145,27,1,0,0,0,146,147,3,32,16,0,147,
        148,3,30,15,0,148,151,1,0,0,0,149,151,3,30,15,0,150,146,1,0,0,0,
        150,149,1,0,0,0,151,29,1,0,0,0,152,156,5,20,0,0,153,156,5,21,0,0,
        154,156,5,22,0,0,155,152,1,0,0,0,155,153,1,0,0,0,155,154,1,0,0,0,
        156,31,1,0,0,0,157,158,5,23,0,0,158,33,1,0,0,0,159,162,5,25,0,0,
        160,162,5,26,0,0,161,159,1,0,0,0,161,160,1,0,0,0,162,35,1,0,0,0,
        163,164,5,24,0,0,164,167,5,7,0,0,165,168,5,29,0,0,166,168,3,26,13,
        0,167,165,1,0,0,0,167,166,1,0,0,0,168,169,1,0,0,0,169,170,5,8,0,
        0,170,37,1,0,0,0,15,41,52,72,83,85,96,107,118,131,138,142,150,155,
        161,167
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
    RULE_type_specifier = 15
    RULE_reserved_word = 16
    RULE_comment = 17
    RULE_printf = 18

    ruleNames =  [ "prog", "instr", "unary_operator", "parenthesis_expression", 
                   "unary_expression", "mul_div_expression", "add_sub_expression", 
                   "relational_expression", "logical_expression", "assignment_expression", 
                   "declaration_specification", "declaration", "expr", "constant", 
                   "type", "type_specifier", "reserved_word", "comment", 
                   "printf" ]

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
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.instr()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2146435324) != 0)):
                    break

            self.state = 43
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
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 6, 7, 20, 21, 22, 23, 27, 28, 29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.expr()
                self.state = 46
                self.match(CGrammarParser.T__0)
                pass
            elif token in [25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.comment()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.printf()
                self.state = 50
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
            self.state = 54
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
            self.state = 56
            self.match(CGrammarParser.T__6)
            self.state = 57
            self.expr()
            self.state = 58
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


        def unary_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Unary_expressionContext,0)


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
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.unary_operator()
                self.state = 61
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.unary_operator()
                self.state = 64
                self.constant()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.constant()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.parenthesis_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 69
                self.unary_operator()
                self.state = 70
                self.unary_expression()
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
            self.state = 75
            self.unary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 83
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 77
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 78
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 79
                        self.unary_expression()
                        pass

                    elif la_ == 2:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 80
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 81
                        self.match(CGrammarParser.T__9)
                        self.state = 82
                        self.unary_expression()
                        pass

             
                self.state = 87
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
            self.state = 89
            self.mul_div_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Add_sub_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expression)
                    self.state = 91
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 92
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==2 or _la==3):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 93
                    self.mul_div_expression(0) 
                self.state = 98
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
            self.state = 100
            self.add_sub_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Relational_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
                    self.state = 102
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 103
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 104
                    self.add_sub_expression(0) 
                self.state = 109
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
            self.state = 111
            self.relational_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 113
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 114
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==18):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 115
                    self.relational_expression(0) 
                self.state = 120
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
            self.state = 121
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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.type_()
                self.state = 124
                self.match(CGrammarParser.T__3)
                self.state = 125
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.type_()
                self.state = 128
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
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
        self.enterRule(localctx, 22, self.RULE_declaration)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                localctx.lvalue = self.declaration_specification()
                self.state = 134
                localctx.assign = self.match(CGrammarParser.T__18)
                self.state = 135
                localctx.rvalue = self.assignment_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
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
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.assignment_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
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
            self.state = 144
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
        self.enterRule(localctx, 28, self.RULE_type)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.reserved_word()
                self.state = 147
                self.type_specifier()
                pass
            elif token in [20, 21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
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
        self.enterRule(localctx, 30, self.RULE_type_specifier)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                localctx.typ = self.match(CGrammarParser.T__19)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                localctx.typ = self.match(CGrammarParser.T__20)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 154
                localctx.typ = self.match(CGrammarParser.T__21)
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
        self.enterRule(localctx, 32, self.RULE_reserved_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
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
        self.enterRule(localctx, 34, self.RULE_comment)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                localctx.block = self.match(CGrammarParser.BLOCKCOMMENT)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
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
        self.enterRule(localctx, 36, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(CGrammarParser.T__23)
            self.state = 164
            self.match(CGrammarParser.T__6)
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.state = 165
                self.match(CGrammarParser.IDENTIFIER)
                pass
            elif token in [27, 28, 30]:
                self.state = 166
                self.constant()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 169
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
         




