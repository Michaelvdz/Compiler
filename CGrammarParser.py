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
        4,1,41,294,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,4,0,50,8,0,11,0,12,0,51,1,
        0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,79,8,5,1,5,1,5,5,5,83,8,5,
        10,5,12,5,86,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,97,8,6,
        10,6,12,6,100,9,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,108,8,7,10,7,12,7,
        111,9,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,119,8,8,10,8,12,8,122,9,8,1,
        9,1,9,1,9,1,9,1,9,1,9,5,9,130,8,9,10,9,12,9,133,9,9,1,10,1,10,1,
        11,1,11,1,11,3,11,140,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,3,12,153,8,12,1,13,1,13,1,13,1,13,1,13,3,13,160,
        8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,3,14,176,8,14,1,14,1,14,5,14,180,8,14,10,14,12,14,183,
        9,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,191,8,15,10,15,12,15,194,
        9,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,204,8,15,10,15,
        12,15,207,9,15,1,15,1,15,1,15,1,15,5,15,213,8,15,10,15,12,15,216,
        9,15,1,15,1,15,3,15,220,8,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,
        228,8,16,10,16,12,16,231,9,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,5,16,245,8,16,10,16,12,16,248,9,16,1,16,
        1,16,1,16,1,16,1,16,1,16,3,16,256,8,16,1,17,1,17,5,17,260,8,17,10,
        17,12,17,263,9,17,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,3,19,273,
        8,19,1,20,1,20,1,20,3,20,278,8,20,1,21,1,21,1,22,1,22,3,22,284,8,
        22,1,23,1,23,1,23,1,23,3,23,290,8,23,1,23,1,23,1,23,0,6,10,12,14,
        16,18,28,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,0,7,1,0,1,5,1,0,6,7,2,0,3,3,10,11,1,0,1,2,1,0,12,
        17,1,0,18,19,2,0,37,38,40,40,308,0,49,1,0,0,0,2,55,1,0,0,0,4,57,
        1,0,0,0,6,59,1,0,0,0,8,61,1,0,0,0,10,78,1,0,0,0,12,87,1,0,0,0,14,
        101,1,0,0,0,16,112,1,0,0,0,18,123,1,0,0,0,20,134,1,0,0,0,22,139,
        1,0,0,0,24,152,1,0,0,0,26,159,1,0,0,0,28,175,1,0,0,0,30,219,1,0,
        0,0,32,255,1,0,0,0,34,257,1,0,0,0,36,266,1,0,0,0,38,272,1,0,0,0,
        40,277,1,0,0,0,42,279,1,0,0,0,44,283,1,0,0,0,46,285,1,0,0,0,48,50,
        3,2,1,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,
        52,53,1,0,0,0,53,54,5,0,0,1,54,1,1,0,0,0,55,56,3,28,14,0,56,3,1,
        0,0,0,57,58,7,0,0,0,58,5,1,0,0,0,59,60,7,1,0,0,60,7,1,0,0,0,61,62,
        5,8,0,0,62,63,3,28,14,0,63,64,5,9,0,0,64,9,1,0,0,0,65,66,6,5,-1,
        0,66,67,3,4,2,0,67,68,5,39,0,0,68,79,1,0,0,0,69,70,3,4,2,0,70,71,
        3,36,18,0,71,79,1,0,0,0,72,79,3,36,18,0,73,79,3,8,4,0,74,79,5,39,
        0,0,75,76,3,4,2,0,76,77,3,10,5,2,77,79,1,0,0,0,78,65,1,0,0,0,78,
        69,1,0,0,0,78,72,1,0,0,0,78,73,1,0,0,0,78,74,1,0,0,0,78,75,1,0,0,
        0,79,84,1,0,0,0,80,81,10,1,0,0,81,83,3,6,3,0,82,80,1,0,0,0,83,86,
        1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,11,1,0,0,0,86,84,1,0,0,0,
        87,88,6,6,-1,0,88,89,3,10,5,0,89,98,1,0,0,0,90,91,10,3,0,0,91,92,
        7,2,0,0,92,97,3,10,5,0,93,94,10,2,0,0,94,95,5,11,0,0,95,97,3,10,
        5,0,96,90,1,0,0,0,96,93,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,
        99,1,0,0,0,99,13,1,0,0,0,100,98,1,0,0,0,101,102,6,7,-1,0,102,103,
        3,12,6,0,103,109,1,0,0,0,104,105,10,2,0,0,105,106,7,3,0,0,106,108,
        3,12,6,0,107,104,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,
        1,0,0,0,110,15,1,0,0,0,111,109,1,0,0,0,112,113,6,8,-1,0,113,114,
        3,14,7,0,114,120,1,0,0,0,115,116,10,2,0,0,116,117,7,4,0,0,117,119,
        3,14,7,0,118,115,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,
        1,0,0,0,121,17,1,0,0,0,122,120,1,0,0,0,123,124,6,9,-1,0,124,125,
        3,16,8,0,125,131,1,0,0,0,126,127,10,2,0,0,127,128,7,5,0,0,128,130,
        3,16,8,0,129,126,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,
        1,0,0,0,132,19,1,0,0,0,133,131,1,0,0,0,134,135,3,18,9,0,135,21,1,
        0,0,0,136,137,5,3,0,0,137,140,3,22,11,0,138,140,5,3,0,0,139,136,
        1,0,0,0,139,138,1,0,0,0,140,23,1,0,0,0,141,142,3,38,19,0,142,143,
        3,22,11,0,143,144,5,39,0,0,144,153,1,0,0,0,145,146,3,38,19,0,146,
        147,5,39,0,0,147,153,1,0,0,0,148,153,5,39,0,0,149,150,3,22,11,0,
        150,151,5,39,0,0,151,153,1,0,0,0,152,141,1,0,0,0,152,145,1,0,0,0,
        152,148,1,0,0,0,152,149,1,0,0,0,153,25,1,0,0,0,154,155,3,24,12,0,
        155,156,5,20,0,0,156,157,3,20,10,0,157,160,1,0,0,0,158,160,3,24,
        12,0,159,154,1,0,0,0,159,158,1,0,0,0,160,27,1,0,0,0,161,162,6,14,
        -1,0,162,163,3,20,10,0,163,164,5,21,0,0,164,176,1,0,0,0,165,166,
        3,26,13,0,166,167,5,21,0,0,167,176,1,0,0,0,168,176,3,30,15,0,169,
        176,3,32,16,0,170,176,3,34,17,0,171,172,3,46,23,0,172,173,5,21,0,
        0,173,176,1,0,0,0,174,176,3,44,22,0,175,161,1,0,0,0,175,165,1,0,
        0,0,175,168,1,0,0,0,175,169,1,0,0,0,175,170,1,0,0,0,175,171,1,0,
        0,0,175,174,1,0,0,0,176,181,1,0,0,0,177,178,10,2,0,0,178,180,3,44,
        22,0,179,177,1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,
        0,0,182,29,1,0,0,0,183,181,1,0,0,0,184,185,5,22,0,0,185,186,5,8,
        0,0,186,187,3,20,10,0,187,188,5,9,0,0,188,192,5,23,0,0,189,191,3,
        28,14,0,190,189,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,
        1,0,0,0,193,195,1,0,0,0,194,192,1,0,0,0,195,196,5,24,0,0,196,220,
        1,0,0,0,197,198,5,22,0,0,198,199,5,8,0,0,199,200,3,20,10,0,200,201,
        5,9,0,0,201,205,5,23,0,0,202,204,3,28,14,0,203,202,1,0,0,0,204,207,
        1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,208,1,0,0,0,207,205,
        1,0,0,0,208,209,5,24,0,0,209,210,5,25,0,0,210,214,5,23,0,0,211,213,
        3,28,14,0,212,211,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,
        1,0,0,0,215,217,1,0,0,0,216,214,1,0,0,0,217,218,5,24,0,0,218,220,
        1,0,0,0,219,184,1,0,0,0,219,197,1,0,0,0,220,31,1,0,0,0,221,222,5,
        26,0,0,222,223,5,8,0,0,223,224,3,20,10,0,224,225,5,9,0,0,225,229,
        5,23,0,0,226,228,3,28,14,0,227,226,1,0,0,0,228,231,1,0,0,0,229,227,
        1,0,0,0,229,230,1,0,0,0,230,232,1,0,0,0,231,229,1,0,0,0,232,233,
        5,24,0,0,233,256,1,0,0,0,234,235,5,27,0,0,235,236,5,8,0,0,236,237,
        3,28,14,0,237,238,5,21,0,0,238,239,3,28,14,0,239,240,5,21,0,0,240,
        241,3,28,14,0,241,242,5,9,0,0,242,246,5,23,0,0,243,245,3,28,14,0,
        244,243,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,
        247,249,1,0,0,0,248,246,1,0,0,0,249,250,5,24,0,0,250,256,1,0,0,0,
        251,252,5,28,0,0,252,256,5,21,0,0,253,254,5,29,0,0,254,256,5,21,
        0,0,255,221,1,0,0,0,255,234,1,0,0,0,255,251,1,0,0,0,255,253,1,0,
        0,0,256,33,1,0,0,0,257,261,5,23,0,0,258,260,3,28,14,0,259,258,1,
        0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,264,1,
        0,0,0,263,261,1,0,0,0,264,265,5,24,0,0,265,35,1,0,0,0,266,267,7,
        6,0,0,267,37,1,0,0,0,268,269,3,42,21,0,269,270,3,40,20,0,270,273,
        1,0,0,0,271,273,3,40,20,0,272,268,1,0,0,0,272,271,1,0,0,0,273,39,
        1,0,0,0,274,278,5,30,0,0,275,278,5,31,0,0,276,278,5,32,0,0,277,274,
        1,0,0,0,277,275,1,0,0,0,277,276,1,0,0,0,278,41,1,0,0,0,279,280,5,
        33,0,0,280,43,1,0,0,0,281,284,5,35,0,0,282,284,5,36,0,0,283,281,
        1,0,0,0,283,282,1,0,0,0,284,45,1,0,0,0,285,286,5,34,0,0,286,289,
        5,8,0,0,287,290,5,39,0,0,288,290,3,36,18,0,289,287,1,0,0,0,289,288,
        1,0,0,0,290,291,1,0,0,0,291,292,5,9,0,0,292,47,1,0,0,0,25,51,78,
        84,96,98,109,120,131,139,152,159,175,181,192,205,214,219,229,246,
        255,261,272,277,283,289
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
    RULE_conditional_statement = 15
    RULE_loops = 16
    RULE_scope = 17
    RULE_constant = 18
    RULE_type = 19
    RULE_type_specifier = 20
    RULE_reserved_word = 21
    RULE_comment = 22
    RULE_printf = 23

    ruleNames =  [ "prog", "instr", "unary_operator", "post_unary_operator", 
                   "parenthesis_expression", "unary_expression", "mul_div_expression", 
                   "add_sub_expression", "relational_expression", "logical_expression", 
                   "assignment_expression", "pointer", "declaration_specification", 
                   "declaration", "expr", "conditional_statement", "loops", 
                   "scope", "constant", "type", "type_specifier", "reserved_word", 
                   "comment", "printf" ]

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
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.instr()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2198968729918) != 0)):
                    break

            self.state = 53
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
            self.state = 55
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
            self.state = 57
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
            self.state = 59
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
            self.state = 61
            self.match(CGrammarParser.T__7)
            self.state = 62
            self.expr(0)
            self.state = 63
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
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 66
                self.unary_operator()
                self.state = 67
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 69
                self.unary_operator()
                self.state = 70
                self.constant()
                pass

            elif la_ == 3:
                self.state = 72
                self.constant()
                pass

            elif la_ == 4:
                self.state = 73
                self.parenthesis_expression()
                pass

            elif la_ == 5:
                self.state = 74
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.state = 75
                self.unary_operator()
                self.state = 76
                self.unary_expression(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Unary_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unary_expression)
                    self.state = 80
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 81
                    self.post_unary_operator() 
                self.state = 86
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
            self.state = 88
            self.unary_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 96
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 90
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 91
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3080) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 92
                        self.unary_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 93
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 94
                        self.match(CGrammarParser.T__10)
                        self.state = 95
                        self.unary_expression(0)
                        pass

             
                self.state = 100
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
            self.state = 102
            self.mul_div_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Add_sub_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expression)
                    self.state = 104
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 105
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 106
                    self.mul_div_expression(0) 
                self.state = 111
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
            self.state = 113
            self.add_sub_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Relational_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
                    self.state = 115
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 116
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 117
                    self.add_sub_expression(0) 
                self.state = 122
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
            self.state = 124
            self.relational_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 126
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 127
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==18 or _la==19):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 128
                    self.relational_expression(0) 
                self.state = 133
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
            self.state = 134
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(CGrammarParser.T__2)
                self.state = 137
                self.pointer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                localctx.typ = self.type_()
                self.state = 142
                localctx.ptr = self.pointer()
                self.state = 143
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                localctx.typ = self.type_()
                self.state = 146
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                localctx.ptr = self.pointer()
                self.state = 150
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
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                localctx.lvalue = self.declaration_specification()
                self.state = 155
                localctx.assign = self.match(CGrammarParser.T__19)
                self.state = 156
                localctx.rvalue = self.assignment_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
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
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 162
                self.assignment_expression()
                self.state = 163
                self.match(CGrammarParser.T__20)
                pass

            elif la_ == 2:
                self.state = 165
                self.declaration()
                self.state = 166
                self.match(CGrammarParser.T__20)
                pass

            elif la_ == 3:
                self.state = 168
                self.conditional_statement()
                pass

            elif la_ == 4:
                self.state = 169
                self.loops()
                pass

            elif la_ == 5:
                self.state = 170
                self.scope()
                pass

            elif la_ == 6:
                self.state = 171
                self.printf()
                self.state = 172
                self.match(CGrammarParser.T__20)
                pass

            elif la_ == 7:
                self.state = 174
                self.comment()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 177
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 178
                    self.comment() 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Conditional_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # Assignment_expressionContext
            self.ifbody = None # ExprContext
            self.elsebody = None # ExprContext

        def assignment_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Assignment_expressionContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(CGrammarParser.ExprContext,i)


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
        self.enterRule(localctx, 30, self.RULE_conditional_statement)
        self._la = 0 # Token type
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(CGrammarParser.T__21)
                self.state = 185
                self.match(CGrammarParser.T__7)
                self.state = 186
                localctx.condition = self.assignment_expression()
                self.state = 187
                self.match(CGrammarParser.T__8)
                self.state = 188
                self.match(CGrammarParser.T__22)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2198968729918) != 0):
                    self.state = 189
                    localctx.ifbody = self.expr(0)
                    self.state = 194
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 195
                self.match(CGrammarParser.T__23)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(CGrammarParser.T__21)
                self.state = 198
                self.match(CGrammarParser.T__7)
                self.state = 199
                localctx.condition = self.assignment_expression()
                self.state = 200
                self.match(CGrammarParser.T__8)
                self.state = 201
                self.match(CGrammarParser.T__22)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2198968729918) != 0):
                    self.state = 202
                    localctx.ifbody = self.expr(0)
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 208
                self.match(CGrammarParser.T__23)
                self.state = 209
                self.match(CGrammarParser.T__24)
                self.state = 210
                self.match(CGrammarParser.T__22)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2198968729918) != 0):
                    self.state = 211
                    localctx.elsebody = self.expr(0)
                    self.state = 216
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 217
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

        def assignment_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Assignment_expressionContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(CGrammarParser.ExprContext,i)


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
        self.enterRule(localctx, 32, self.RULE_loops)
        self._la = 0 # Token type
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(CGrammarParser.T__25)
                self.state = 222
                self.match(CGrammarParser.T__7)
                self.state = 223
                self.assignment_expression()
                self.state = 224
                self.match(CGrammarParser.T__8)
                self.state = 225
                self.match(CGrammarParser.T__22)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2198968729918) != 0):
                    self.state = 226
                    self.expr(0)
                    self.state = 231
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 232
                self.match(CGrammarParser.T__23)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(CGrammarParser.T__26)
                self.state = 235
                self.match(CGrammarParser.T__7)
                self.state = 236
                self.expr(0)
                self.state = 237
                self.match(CGrammarParser.T__20)
                self.state = 238
                self.expr(0)
                self.state = 239
                self.match(CGrammarParser.T__20)
                self.state = 240
                self.expr(0)
                self.state = 241
                self.match(CGrammarParser.T__8)
                self.state = 242
                self.match(CGrammarParser.T__22)
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2198968729918) != 0):
                    self.state = 243
                    self.expr(0)
                    self.state = 248
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 249
                self.match(CGrammarParser.T__23)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.match(CGrammarParser.T__27)
                self.state = 252
                self.match(CGrammarParser.T__20)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.match(CGrammarParser.T__28)
                self.state = 254
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
        self.enterRule(localctx, 34, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            localctx.startscope = self.match(CGrammarParser.T__22)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2198968729918) != 0):
                self.state = 258
                self.expr(0)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 264
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
        self.enterRule(localctx, 36, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
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
        self.enterRule(localctx, 38, self.RULE_type)
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.reserved_word()
                self.state = 269
                self.type_specifier()
                pass
            elif token in [30, 31, 32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
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
        self.enterRule(localctx, 40, self.RULE_type_specifier)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                localctx.typ = self.match(CGrammarParser.T__29)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                localctx.typ = self.match(CGrammarParser.T__30)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
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
        self.enterRule(localctx, 42, self.RULE_reserved_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
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
        self.enterRule(localctx, 44, self.RULE_comment)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                localctx.block = self.match(CGrammarParser.BLOCKCOMMENT)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
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
        self.enterRule(localctx, 46, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(CGrammarParser.T__33)
            self.state = 286
            self.match(CGrammarParser.T__7)
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 287
                self.match(CGrammarParser.IDENTIFIER)
                pass
            elif token in [37, 38, 40]:
                self.state = 288
                self.constant()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 291
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
                return self.precpred(self._ctx, 2)
         




