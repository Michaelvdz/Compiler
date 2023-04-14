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
        4,1,41,284,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,4,0,54,
        8,0,11,0,12,0,55,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,83,8,5,1,
        5,1,5,5,5,87,8,5,10,5,12,5,90,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,5,6,101,8,6,10,6,12,6,104,9,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,
        112,8,7,10,7,12,7,115,9,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,123,8,8,10,
        8,12,8,126,9,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,134,8,9,10,9,12,9,137,
        9,9,1,10,1,10,1,11,1,11,1,11,3,11,144,8,11,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,157,8,12,1,13,1,13,1,13,1,
        13,1,13,3,13,164,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,181,8,14,1,14,1,14,5,14,185,
        8,14,10,14,12,14,188,9,14,1,15,5,15,191,8,15,10,15,12,15,194,9,15,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,216,8,16,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,
        233,8,17,1,17,1,17,1,17,1,17,1,17,3,17,240,8,17,1,18,1,18,1,18,1,
        18,3,18,246,8,18,1,19,1,19,5,19,250,8,19,10,19,12,19,253,9,19,1,
        19,1,19,1,20,1,20,1,21,1,21,1,21,1,21,3,21,263,8,21,1,22,1,22,1,
        22,3,22,268,8,22,1,23,1,23,1,24,1,24,3,24,274,8,24,1,25,1,25,1,25,
        1,25,3,25,280,8,25,1,25,1,25,1,25,0,6,10,12,14,16,18,28,26,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,0,7,1,0,1,5,1,0,6,7,2,0,3,3,10,11,1,0,1,2,1,0,12,17,1,0,18,19,
        2,0,37,38,40,40,293,0,53,1,0,0,0,2,59,1,0,0,0,4,61,1,0,0,0,6,63,
        1,0,0,0,8,65,1,0,0,0,10,82,1,0,0,0,12,91,1,0,0,0,14,105,1,0,0,0,
        16,116,1,0,0,0,18,127,1,0,0,0,20,138,1,0,0,0,22,143,1,0,0,0,24,156,
        1,0,0,0,26,163,1,0,0,0,28,180,1,0,0,0,30,192,1,0,0,0,32,215,1,0,
        0,0,34,239,1,0,0,0,36,245,1,0,0,0,38,247,1,0,0,0,40,256,1,0,0,0,
        42,262,1,0,0,0,44,267,1,0,0,0,46,269,1,0,0,0,48,273,1,0,0,0,50,275,
        1,0,0,0,52,54,3,2,1,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,
        55,56,1,0,0,0,56,57,1,0,0,0,57,58,5,0,0,1,58,1,1,0,0,0,59,60,3,28,
        14,0,60,3,1,0,0,0,61,62,7,0,0,0,62,5,1,0,0,0,63,64,7,1,0,0,64,7,
        1,0,0,0,65,66,5,8,0,0,66,67,3,20,10,0,67,68,5,9,0,0,68,9,1,0,0,0,
        69,70,6,5,-1,0,70,71,3,4,2,0,71,72,5,39,0,0,72,83,1,0,0,0,73,74,
        3,4,2,0,74,75,3,40,20,0,75,83,1,0,0,0,76,83,3,40,20,0,77,83,3,8,
        4,0,78,83,5,39,0,0,79,80,3,4,2,0,80,81,3,10,5,2,81,83,1,0,0,0,82,
        69,1,0,0,0,82,73,1,0,0,0,82,76,1,0,0,0,82,77,1,0,0,0,82,78,1,0,0,
        0,82,79,1,0,0,0,83,88,1,0,0,0,84,85,10,1,0,0,85,87,3,6,3,0,86,84,
        1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,11,1,0,0,0,
        90,88,1,0,0,0,91,92,6,6,-1,0,92,93,3,10,5,0,93,102,1,0,0,0,94,95,
        10,3,0,0,95,96,7,2,0,0,96,101,3,10,5,0,97,98,10,2,0,0,98,99,5,11,
        0,0,99,101,3,10,5,0,100,94,1,0,0,0,100,97,1,0,0,0,101,104,1,0,0,
        0,102,100,1,0,0,0,102,103,1,0,0,0,103,13,1,0,0,0,104,102,1,0,0,0,
        105,106,6,7,-1,0,106,107,3,12,6,0,107,113,1,0,0,0,108,109,10,2,0,
        0,109,110,7,3,0,0,110,112,3,12,6,0,111,108,1,0,0,0,112,115,1,0,0,
        0,113,111,1,0,0,0,113,114,1,0,0,0,114,15,1,0,0,0,115,113,1,0,0,0,
        116,117,6,8,-1,0,117,118,3,14,7,0,118,124,1,0,0,0,119,120,10,2,0,
        0,120,121,7,4,0,0,121,123,3,14,7,0,122,119,1,0,0,0,123,126,1,0,0,
        0,124,122,1,0,0,0,124,125,1,0,0,0,125,17,1,0,0,0,126,124,1,0,0,0,
        127,128,6,9,-1,0,128,129,3,16,8,0,129,135,1,0,0,0,130,131,10,2,0,
        0,131,132,7,5,0,0,132,134,3,16,8,0,133,130,1,0,0,0,134,137,1,0,0,
        0,135,133,1,0,0,0,135,136,1,0,0,0,136,19,1,0,0,0,137,135,1,0,0,0,
        138,139,3,18,9,0,139,21,1,0,0,0,140,141,5,3,0,0,141,144,3,22,11,
        0,142,144,5,3,0,0,143,140,1,0,0,0,143,142,1,0,0,0,144,23,1,0,0,0,
        145,146,3,42,21,0,146,147,3,22,11,0,147,148,5,39,0,0,148,157,1,0,
        0,0,149,150,3,42,21,0,150,151,5,39,0,0,151,157,1,0,0,0,152,157,5,
        39,0,0,153,154,3,22,11,0,154,155,5,39,0,0,155,157,1,0,0,0,156,145,
        1,0,0,0,156,149,1,0,0,0,156,152,1,0,0,0,156,153,1,0,0,0,157,25,1,
        0,0,0,158,159,3,24,12,0,159,160,5,20,0,0,160,161,3,20,10,0,161,164,
        1,0,0,0,162,164,3,24,12,0,163,158,1,0,0,0,163,162,1,0,0,0,164,27,
        1,0,0,0,165,166,6,14,-1,0,166,167,3,20,10,0,167,168,5,21,0,0,168,
        181,1,0,0,0,169,170,3,26,13,0,170,171,5,21,0,0,171,181,1,0,0,0,172,
        181,3,32,16,0,173,181,3,34,17,0,174,181,3,38,19,0,175,176,3,50,25,
        0,176,177,5,21,0,0,177,181,1,0,0,0,178,181,3,48,24,0,179,181,3,36,
        18,0,180,165,1,0,0,0,180,169,1,0,0,0,180,172,1,0,0,0,180,173,1,0,
        0,0,180,174,1,0,0,0,180,175,1,0,0,0,180,178,1,0,0,0,180,179,1,0,
        0,0,181,186,1,0,0,0,182,183,10,3,0,0,183,185,3,48,24,0,184,182,1,
        0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,29,1,0,
        0,0,188,186,1,0,0,0,189,191,3,28,14,0,190,189,1,0,0,0,191,194,1,
        0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,31,1,0,0,0,194,192,1,0,
        0,0,195,196,5,22,0,0,196,197,5,8,0,0,197,198,3,20,10,0,198,199,5,
        9,0,0,199,200,5,23,0,0,200,201,3,30,15,0,201,202,5,24,0,0,202,216,
        1,0,0,0,203,204,5,22,0,0,204,205,5,8,0,0,205,206,3,20,10,0,206,207,
        5,9,0,0,207,208,5,23,0,0,208,209,3,30,15,0,209,210,5,24,0,0,210,
        211,5,25,0,0,211,212,5,23,0,0,212,213,3,30,15,0,213,214,5,24,0,0,
        214,216,1,0,0,0,215,195,1,0,0,0,215,203,1,0,0,0,216,33,1,0,0,0,217,
        218,5,26,0,0,218,219,5,8,0,0,219,220,3,20,10,0,220,221,5,9,0,0,221,
        222,5,23,0,0,222,223,3,30,15,0,223,224,5,24,0,0,224,240,1,0,0,0,
        225,226,5,27,0,0,226,227,5,8,0,0,227,228,3,26,13,0,228,229,5,21,
        0,0,229,230,3,20,10,0,230,232,5,21,0,0,231,233,3,20,10,0,232,231,
        1,0,0,0,232,233,1,0,0,0,233,234,1,0,0,0,234,235,5,9,0,0,235,236,
        5,23,0,0,236,237,3,30,15,0,237,238,5,24,0,0,238,240,1,0,0,0,239,
        217,1,0,0,0,239,225,1,0,0,0,240,35,1,0,0,0,241,242,5,28,0,0,242,
        246,5,21,0,0,243,244,5,29,0,0,244,246,5,21,0,0,245,241,1,0,0,0,245,
        243,1,0,0,0,246,37,1,0,0,0,247,251,5,23,0,0,248,250,3,28,14,0,249,
        248,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,
        254,1,0,0,0,253,251,1,0,0,0,254,255,5,24,0,0,255,39,1,0,0,0,256,
        257,7,6,0,0,257,41,1,0,0,0,258,259,3,46,23,0,259,260,3,44,22,0,260,
        263,1,0,0,0,261,263,3,44,22,0,262,258,1,0,0,0,262,261,1,0,0,0,263,
        43,1,0,0,0,264,268,5,30,0,0,265,268,5,31,0,0,266,268,5,32,0,0,267,
        264,1,0,0,0,267,265,1,0,0,0,267,266,1,0,0,0,268,45,1,0,0,0,269,270,
        5,33,0,0,270,47,1,0,0,0,271,274,5,35,0,0,272,274,5,36,0,0,273,271,
        1,0,0,0,273,272,1,0,0,0,274,49,1,0,0,0,275,276,5,34,0,0,276,279,
        5,8,0,0,277,280,5,39,0,0,278,280,3,40,20,0,279,277,1,0,0,0,279,278,
        1,0,0,0,280,281,1,0,0,0,281,282,5,9,0,0,282,51,1,0,0,0,23,55,82,
        88,100,102,113,124,135,143,156,163,180,186,192,215,232,239,245,251,
        262,267,273,279
    ]

class CGrammarParser ( Parser ):

    grammarFileName = "CGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'&'", "'!'", "'++'", 
                     "'--'", "'('", "')'", "'/'", "'%'", "'<'", "'>'", "'=='", 
                     "'<='", "'>='", "'!='", "'&&'", "'||'", "'='", "';'", 
                     "'if'", "'{'", "'}'", "'else'", "'while'", "'for'", 
                     "'break'", "'continue'", "'int'", "'float'", "'char'", 
                     "'const'", "'printf'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BLOCKCOMMENT", 
                      "SINGLE_LINE_COMMENT", "INT", "FLOAT", "IDENTIFIER", 
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
    RULE_pointer = 11
    RULE_declaration_specification = 12
    RULE_declaration = 13
    RULE_expr = 14
    RULE_expr_loop = 15
    RULE_conditional_statement = 16
    RULE_loops = 17
    RULE_jumps = 18
    RULE_scope = 19
    RULE_constant = 20
    RULE_type = 21
    RULE_type_specifier = 22
    RULE_reserved_word = 23
    RULE_comment = 24
    RULE_printf = 25

    ruleNames =  [ "prog", "instr", "unary_operator", "post_unary_operator", 
                   "parenthesis_expression", "unary_expression", "mul_div_expression", 
                   "add_sub_expression", "relational_expression", "logical_expression", 
                   "assignment_expression", "pointer", "declaration_specification", 
                   "declaration", "expr", "expr_loop", "conditional_statement", 
                   "loops", "jumps", "scope", "constant", "type", "type_specifier", 
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
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    BLOCKCOMMENT=35
    SINGLE_LINE_COMMENT=36
    INT=37
    FLOAT=38
    IDENTIFIER=39
    CHAR=40
    WS=41

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
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self.instr()
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2198968729918) != 0)):
                    break

            self.state = 57
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
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.expr(0)
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
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
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
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
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

        def assignment_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Assignment_expressionContext,0)


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
            self.state = 65
            self.match(CGrammarParser.T__7)
            self.state = 66
            self.assignment_expression()
            self.state = 67
            self.match(CGrammarParser.T__8)
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
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 70
                self.unary_operator()
                self.state = 71
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 73
                self.unary_operator()
                self.state = 74
                self.constant()
                pass

            elif la_ == 3:
                self.state = 76
                self.constant()
                pass

            elif la_ == 4:
                self.state = 77
                self.parenthesis_expression()
                pass

            elif la_ == 5:
                self.state = 78
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.state = 79
                self.unary_operator()
                self.state = 80
                self.unary_expression(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Unary_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unary_expression)
                    self.state = 84
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 85
                    self.post_unary_operator() 
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            self.state = 92
            self.unary_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 100
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 94
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 95
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3080) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 96
                        self.unary_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 97
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 98
                        self.match(CGrammarParser.T__10)
                        self.state = 99
                        self.unary_expression(0)
                        pass

             
                self.state = 104
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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_add_sub_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.mul_div_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Add_sub_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expression)
                    self.state = 108
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 109
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 110
                    self.mul_div_expression(0) 
                self.state = 115
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_relational_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.add_sub_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Relational_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
                    self.state = 119
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 120
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 121
                    self.add_sub_expression(0) 
                self.state = 126
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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_logical_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.relational_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 130
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 131
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==18 or _la==19):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 132
                    self.relational_expression(0) 
                self.state = 137
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
        self.enterRule(localctx, 20, self.RULE_assignment_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.logical_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pointer(self):
            return self.getTypedRuleContext(CGrammarParser.PointerContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_pointer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointer" ):
                listener.enterPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointer" ):
                listener.exitPointer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointer" ):
                return visitor.visitPointer(self)
            else:
                return visitor.visitChildren(self)




    def pointer(self):

        localctx = CGrammarParser.PointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_pointer)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(CGrammarParser.T__2)
                self.state = 141
                self.pointer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(CGrammarParser.T__2)
                pass


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
            self.typ = None # TypeContext
            self.ptr = None # PointerContext
            self.var = None # Token

        def type_(self):
            return self.getTypedRuleContext(CGrammarParser.TypeContext,0)


        def pointer(self):
            return self.getTypedRuleContext(CGrammarParser.PointerContext,0)


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
        self.enterRule(localctx, 24, self.RULE_declaration_specification)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                localctx.typ = self.type_()
                self.state = 146
                localctx.ptr = self.pointer()
                self.state = 147
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                localctx.typ = self.type_()
                self.state = 150
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                localctx.ptr = self.pointer()
                self.state = 154
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
        self.enterRule(localctx, 26, self.RULE_declaration)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                localctx.lvalue = self.declaration_specification()
                self.state = 159
                localctx.assign = self.match(CGrammarParser.T__19)
                self.state = 160
                localctx.rvalue = self.assignment_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
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


        def conditional_statement(self):
            return self.getTypedRuleContext(CGrammarParser.Conditional_statementContext,0)


        def loops(self):
            return self.getTypedRuleContext(CGrammarParser.LoopsContext,0)


        def scope(self):
            return self.getTypedRuleContext(CGrammarParser.ScopeContext,0)


        def printf(self):
            return self.getTypedRuleContext(CGrammarParser.PrintfContext,0)


        def comment(self):
            return self.getTypedRuleContext(CGrammarParser.CommentContext,0)


        def jumps(self):
            return self.getTypedRuleContext(CGrammarParser.JumpsContext,0)


        def expr(self):
            return self.getTypedRuleContext(CGrammarParser.ExprContext,0)


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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 166
                self.assignment_expression()
                self.state = 167
                self.match(CGrammarParser.T__20)
                pass

            elif la_ == 2:
                self.state = 169
                self.declaration()
                self.state = 170
                self.match(CGrammarParser.T__20)
                pass

            elif la_ == 3:
                self.state = 172
                self.conditional_statement()
                pass

            elif la_ == 4:
                self.state = 173
                self.loops()
                pass

            elif la_ == 5:
                self.state = 174
                self.scope()
                pass

            elif la_ == 6:
                self.state = 175
                self.printf()
                self.state = 176
                self.match(CGrammarParser.T__20)
                pass

            elif la_ == 7:
                self.state = 178
                self.comment()
                pass

            elif la_ == 8:
                self.state = 179
                self.jumps()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 182
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 183
                    self.comment() 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(CGrammarParser.ExprContext,i)


        def getRuleIndex(self):
            return CGrammarParser.RULE_expr_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_loop" ):
                listener.enterExpr_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_loop" ):
                listener.exitExpr_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_loop" ):
                return visitor.visitExpr_loop(self)
            else:
                return visitor.visitChildren(self)




    def expr_loop(self):

        localctx = CGrammarParser.Expr_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2198968729918) != 0):
                self.state = 189
                self.expr(0)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conditional_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # Assignment_expressionContext
            self.ifbody = None # Expr_loopContext
            self.elsebody = None # Expr_loopContext

        def assignment_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Assignment_expressionContext,0)


        def expr_loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CGrammarParser.Expr_loopContext)
            else:
                return self.getTypedRuleContext(CGrammarParser.Expr_loopContext,i)


        def getRuleIndex(self):
            return CGrammarParser.RULE_conditional_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_statement" ):
                listener.enterConditional_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_statement" ):
                listener.exitConditional_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_statement" ):
                return visitor.visitConditional_statement(self)
            else:
                return visitor.visitChildren(self)




    def conditional_statement(self):

        localctx = CGrammarParser.Conditional_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_conditional_statement)
        try:
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(CGrammarParser.T__21)
                self.state = 196
                self.match(CGrammarParser.T__7)
                self.state = 197
                localctx.condition = self.assignment_expression()
                self.state = 198
                self.match(CGrammarParser.T__8)
                self.state = 199
                self.match(CGrammarParser.T__22)
                self.state = 200
                localctx.ifbody = self.expr_loop()
                self.state = 201
                self.match(CGrammarParser.T__23)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(CGrammarParser.T__21)
                self.state = 204
                self.match(CGrammarParser.T__7)
                self.state = 205
                localctx.condition = self.assignment_expression()
                self.state = 206
                self.match(CGrammarParser.T__8)
                self.state = 207
                self.match(CGrammarParser.T__22)
                self.state = 208
                localctx.ifbody = self.expr_loop()
                self.state = 209
                self.match(CGrammarParser.T__23)
                self.state = 210
                self.match(CGrammarParser.T__24)
                self.state = 211
                self.match(CGrammarParser.T__22)
                self.state = 212
                localctx.elsebody = self.expr_loop()
                self.state = 213
                self.match(CGrammarParser.T__23)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.loop = None # Token
            self.condition = None # Assignment_expressionContext
            self.body = None # Expr_loopContext
            self.before = None # DeclarationContext
            self.after = None # Assignment_expressionContext

        def assignment_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CGrammarParser.Assignment_expressionContext)
            else:
                return self.getTypedRuleContext(CGrammarParser.Assignment_expressionContext,i)


        def expr_loop(self):
            return self.getTypedRuleContext(CGrammarParser.Expr_loopContext,0)


        def declaration(self):
            return self.getTypedRuleContext(CGrammarParser.DeclarationContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_loops

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoops" ):
                listener.enterLoops(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoops" ):
                listener.exitLoops(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoops" ):
                return visitor.visitLoops(self)
            else:
                return visitor.visitChildren(self)




    def loops(self):

        localctx = CGrammarParser.LoopsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_loops)
        self._la = 0 # Token type
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                localctx.loop = self.match(CGrammarParser.T__25)
                self.state = 218
                self.match(CGrammarParser.T__7)
                self.state = 219
                localctx.condition = self.assignment_expression()
                self.state = 220
                self.match(CGrammarParser.T__8)
                self.state = 221
                self.match(CGrammarParser.T__22)
                self.state = 222
                localctx.body = self.expr_loop()
                self.state = 223
                self.match(CGrammarParser.T__23)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                localctx.loop = self.match(CGrammarParser.T__26)
                self.state = 226
                self.match(CGrammarParser.T__7)
                self.state = 227
                localctx.before = self.declaration()
                self.state = 228
                self.match(CGrammarParser.T__20)
                self.state = 229
                localctx.condition = self.assignment_expression()
                self.state = 230
                self.match(CGrammarParser.T__20)
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2061584302398) != 0):
                    self.state = 231
                    localctx.after = self.assignment_expression()


                self.state = 234
                self.match(CGrammarParser.T__8)
                self.state = 235
                self.match(CGrammarParser.T__22)
                self.state = 236
                localctx.body = self.expr_loop()
                self.state = 237
                self.match(CGrammarParser.T__23)
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


    class JumpsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.jump = None # Token


        def getRuleIndex(self):
            return CGrammarParser.RULE_jumps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumps" ):
                listener.enterJumps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumps" ):
                listener.exitJumps(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumps" ):
                return visitor.visitJumps(self)
            else:
                return visitor.visitChildren(self)




    def jumps(self):

        localctx = CGrammarParser.JumpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_jumps)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                localctx.jump = self.match(CGrammarParser.T__27)
                self.state = 242
                self.match(CGrammarParser.T__20)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                localctx.jump = self.match(CGrammarParser.T__28)
                self.state = 244
                self.match(CGrammarParser.T__20)
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


    class ScopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.startscope = None # Token
            self.endscope = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(CGrammarParser.ExprContext,i)


        def getRuleIndex(self):
            return CGrammarParser.RULE_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScope" ):
                listener.enterScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScope" ):
                listener.exitScope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScope" ):
                return visitor.visitScope(self)
            else:
                return visitor.visitChildren(self)




    def scope(self):

        localctx = CGrammarParser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            localctx.startscope = self.match(CGrammarParser.T__22)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2198968729918) != 0):
                self.state = 248
                self.expr(0)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 254
            localctx.endscope = self.match(CGrammarParser.T__23)
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
        self.enterRule(localctx, 40, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1511828488192) != 0)):
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
        self.enterRule(localctx, 42, self.RULE_type)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.reserved_word()
                self.state = 259
                self.type_specifier()
                pass
            elif token in [30, 31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
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
        self.enterRule(localctx, 44, self.RULE_type_specifier)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                localctx.typ = self.match(CGrammarParser.T__29)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                localctx.typ = self.match(CGrammarParser.T__30)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                localctx.typ = self.match(CGrammarParser.T__31)
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
        self.enterRule(localctx, 46, self.RULE_reserved_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(CGrammarParser.T__32)
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

        def SINGLE_LINE_COMMENT(self):
            return self.getToken(CGrammarParser.SINGLE_LINE_COMMENT, 0)

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
        self.enterRule(localctx, 48, self.RULE_comment)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                localctx.block = self.match(CGrammarParser.BLOCKCOMMENT)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                localctx.sl = self.match(CGrammarParser.SINGLE_LINE_COMMENT)
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
        self.enterRule(localctx, 50, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(CGrammarParser.T__33)
            self.state = 276
            self.match(CGrammarParser.T__7)
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 277
                self.match(CGrammarParser.IDENTIFIER)
                pass
            elif token in [37, 38, 40]:
                self.state = 278
                self.constant()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 281
            self.match(CGrammarParser.T__8)
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
        self._predicates[14] = self.expr_sempred
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
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




