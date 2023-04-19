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
        4,1,44,372,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,4,0,64,8,0,11,0,12,0,
        65,1,0,1,0,1,1,1,1,1,1,3,1,73,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,3,4,87,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,107,8,6,1,6,1,6,5,6,111,
        8,6,10,6,12,6,114,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,125,
        8,7,10,7,12,7,128,9,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,136,8,8,10,8,12,
        8,139,9,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,147,8,9,10,9,12,9,150,9,9,
        1,10,1,10,1,10,1,10,1,10,1,10,5,10,158,8,10,10,10,12,10,161,9,10,
        1,11,1,11,1,11,1,11,1,11,3,11,168,8,11,1,12,1,12,1,12,3,12,173,8,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,186,
        8,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,3,15,206,8,15,1,15,1,15,5,15,210,8,
        15,10,15,12,15,213,9,15,1,16,5,16,216,8,16,10,16,12,16,219,9,16,
        1,17,1,17,1,17,1,17,1,17,3,17,226,8,17,1,18,1,18,1,18,1,18,1,18,
        1,18,5,18,234,8,18,10,18,12,18,237,9,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,3,19,249,8,19,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,
        281,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,303,8,21,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,3,22,320,8,22,1,22,1,22,1,22,1,22,1,22,3,22,327,8,22,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,339,8,23,1,24,1,
        24,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,26,3,26,351,8,26,1,27,1,
        27,1,27,3,27,356,8,27,1,28,1,28,1,29,1,29,3,29,362,8,29,1,30,1,30,
        1,30,1,30,3,30,368,8,30,1,30,1,30,1,30,0,7,12,14,16,18,20,30,36,
        31,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,0,7,1,0,2,6,1,0,7,8,2,0,4,4,11,12,1,0,
        2,3,1,0,13,18,1,0,19,20,2,0,39,40,42,42,390,0,63,1,0,0,0,2,72,1,
        0,0,0,4,74,1,0,0,0,6,76,1,0,0,0,8,86,1,0,0,0,10,88,1,0,0,0,12,106,
        1,0,0,0,14,115,1,0,0,0,16,129,1,0,0,0,18,140,1,0,0,0,20,151,1,0,
        0,0,22,167,1,0,0,0,24,172,1,0,0,0,26,185,1,0,0,0,28,187,1,0,0,0,
        30,205,1,0,0,0,32,217,1,0,0,0,34,225,1,0,0,0,36,227,1,0,0,0,38,248,
        1,0,0,0,40,280,1,0,0,0,42,302,1,0,0,0,44,326,1,0,0,0,46,338,1,0,
        0,0,48,340,1,0,0,0,50,344,1,0,0,0,52,350,1,0,0,0,54,355,1,0,0,0,
        56,357,1,0,0,0,58,361,1,0,0,0,60,363,1,0,0,0,62,64,3,2,1,0,63,62,
        1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,
        67,68,5,0,0,1,68,1,1,0,0,0,69,73,3,30,15,0,70,73,5,43,0,0,71,73,
        5,1,0,0,72,69,1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,0,73,3,1,0,0,0,74,
        75,7,0,0,0,75,5,1,0,0,0,76,77,7,1,0,0,77,7,1,0,0,0,78,79,5,41,0,
        0,79,80,5,9,0,0,80,87,5,10,0,0,81,82,5,41,0,0,82,83,5,9,0,0,83,84,
        3,34,17,0,84,85,5,10,0,0,85,87,1,0,0,0,86,78,1,0,0,0,86,81,1,0,0,
        0,87,9,1,0,0,0,88,89,5,9,0,0,89,90,3,22,11,0,90,91,5,10,0,0,91,11,
        1,0,0,0,92,93,6,6,-1,0,93,94,3,4,2,0,94,95,5,41,0,0,95,107,1,0,0,
        0,96,97,3,4,2,0,97,98,3,50,25,0,98,107,1,0,0,0,99,107,3,50,25,0,
        100,107,3,10,5,0,101,107,5,41,0,0,102,103,3,4,2,0,103,104,3,12,6,
        3,104,107,1,0,0,0,105,107,3,8,4,0,106,92,1,0,0,0,106,96,1,0,0,0,
        106,99,1,0,0,0,106,100,1,0,0,0,106,101,1,0,0,0,106,102,1,0,0,0,106,
        105,1,0,0,0,107,112,1,0,0,0,108,109,10,2,0,0,109,111,3,6,3,0,110,
        108,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,
        13,1,0,0,0,114,112,1,0,0,0,115,116,6,7,-1,0,116,117,3,12,6,0,117,
        126,1,0,0,0,118,119,10,3,0,0,119,120,7,2,0,0,120,125,3,12,6,0,121,
        122,10,2,0,0,122,123,5,12,0,0,123,125,3,12,6,0,124,118,1,0,0,0,124,
        121,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,
        15,1,0,0,0,128,126,1,0,0,0,129,130,6,8,-1,0,130,131,3,14,7,0,131,
        137,1,0,0,0,132,133,10,2,0,0,133,134,7,3,0,0,134,136,3,14,7,0,135,
        132,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,
        17,1,0,0,0,139,137,1,0,0,0,140,141,6,9,-1,0,141,142,3,16,8,0,142,
        148,1,0,0,0,143,144,10,2,0,0,144,145,7,4,0,0,145,147,3,16,8,0,146,
        143,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,
        19,1,0,0,0,150,148,1,0,0,0,151,152,6,10,-1,0,152,153,3,18,9,0,153,
        159,1,0,0,0,154,155,10,2,0,0,155,156,7,5,0,0,156,158,3,18,9,0,157,
        154,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,
        21,1,0,0,0,161,159,1,0,0,0,162,168,3,20,10,0,163,164,3,26,13,0,164,
        165,5,21,0,0,165,166,3,22,11,0,166,168,1,0,0,0,167,162,1,0,0,0,167,
        163,1,0,0,0,168,23,1,0,0,0,169,170,5,4,0,0,170,173,3,24,12,0,171,
        173,5,4,0,0,172,169,1,0,0,0,172,171,1,0,0,0,173,25,1,0,0,0,174,175,
        3,52,26,0,175,176,3,24,12,0,176,177,5,41,0,0,177,186,1,0,0,0,178,
        179,3,52,26,0,179,180,5,41,0,0,180,186,1,0,0,0,181,186,5,41,0,0,
        182,183,3,24,12,0,183,184,5,41,0,0,184,186,1,0,0,0,185,174,1,0,0,
        0,185,178,1,0,0,0,185,181,1,0,0,0,185,182,1,0,0,0,186,27,1,0,0,0,
        187,188,3,26,13,0,188,29,1,0,0,0,189,190,6,15,-1,0,190,191,3,22,
        11,0,191,192,5,1,0,0,192,206,1,0,0,0,193,194,3,28,14,0,194,195,5,
        1,0,0,195,206,1,0,0,0,196,206,3,42,21,0,197,206,3,44,22,0,198,206,
        3,48,24,0,199,200,3,60,30,0,200,201,5,1,0,0,201,206,1,0,0,0,202,
        206,3,58,29,0,203,206,3,46,23,0,204,206,3,40,20,0,205,189,1,0,0,
        0,205,193,1,0,0,0,205,196,1,0,0,0,205,197,1,0,0,0,205,198,1,0,0,
        0,205,199,1,0,0,0,205,202,1,0,0,0,205,203,1,0,0,0,205,204,1,0,0,
        0,206,211,1,0,0,0,207,208,10,4,0,0,208,210,3,58,29,0,209,207,1,0,
        0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,31,1,0,0,
        0,213,211,1,0,0,0,214,216,3,30,15,0,215,214,1,0,0,0,216,219,1,0,
        0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,33,1,0,0,0,219,217,1,0,0,
        0,220,226,3,22,11,0,221,222,3,22,11,0,222,223,5,22,0,0,223,224,3,
        34,17,0,224,226,1,0,0,0,225,220,1,0,0,0,225,221,1,0,0,0,226,35,1,
        0,0,0,227,228,6,18,-1,0,228,229,5,41,0,0,229,235,1,0,0,0,230,231,
        10,1,0,0,231,232,5,22,0,0,232,234,5,41,0,0,233,230,1,0,0,0,234,237,
        1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,37,1,0,0,0,237,235,1,
        0,0,0,238,249,3,52,26,0,239,249,3,28,14,0,240,241,3,52,26,0,241,
        242,5,22,0,0,242,243,3,38,19,0,243,249,1,0,0,0,244,245,3,28,14,0,
        245,246,5,22,0,0,246,247,3,38,19,0,247,249,1,0,0,0,248,238,1,0,0,
        0,248,239,1,0,0,0,248,240,1,0,0,0,248,244,1,0,0,0,249,39,1,0,0,0,
        250,251,3,54,27,0,251,252,5,41,0,0,252,253,5,9,0,0,253,254,3,38,
        19,0,254,255,5,10,0,0,255,256,5,23,0,0,256,257,3,32,16,0,257,258,
        5,24,0,0,258,281,1,0,0,0,259,260,3,54,27,0,260,261,5,41,0,0,261,
        262,5,9,0,0,262,263,3,38,19,0,263,264,5,10,0,0,264,265,5,1,0,0,265,
        281,1,0,0,0,266,267,3,54,27,0,267,268,5,41,0,0,268,269,5,9,0,0,269,
        270,5,10,0,0,270,271,5,23,0,0,271,272,3,32,16,0,272,273,5,24,0,0,
        273,281,1,0,0,0,274,275,3,54,27,0,275,276,5,41,0,0,276,277,5,9,0,
        0,277,278,5,10,0,0,278,279,5,1,0,0,279,281,1,0,0,0,280,250,1,0,0,
        0,280,259,1,0,0,0,280,266,1,0,0,0,280,274,1,0,0,0,281,41,1,0,0,0,
        282,283,5,25,0,0,283,284,5,9,0,0,284,285,3,22,11,0,285,286,5,10,
        0,0,286,287,5,23,0,0,287,288,3,32,16,0,288,289,5,24,0,0,289,303,
        1,0,0,0,290,291,5,25,0,0,291,292,5,9,0,0,292,293,3,22,11,0,293,294,
        5,10,0,0,294,295,5,23,0,0,295,296,3,32,16,0,296,297,5,24,0,0,297,
        298,5,26,0,0,298,299,5,23,0,0,299,300,3,32,16,0,300,301,5,24,0,0,
        301,303,1,0,0,0,302,282,1,0,0,0,302,290,1,0,0,0,303,43,1,0,0,0,304,
        305,5,27,0,0,305,306,5,9,0,0,306,307,3,22,11,0,307,308,5,10,0,0,
        308,309,5,23,0,0,309,310,3,32,16,0,310,311,5,24,0,0,311,327,1,0,
        0,0,312,313,5,28,0,0,313,314,5,9,0,0,314,315,3,28,14,0,315,316,5,
        1,0,0,316,317,3,22,11,0,317,319,5,1,0,0,318,320,3,22,11,0,319,318,
        1,0,0,0,319,320,1,0,0,0,320,321,1,0,0,0,321,322,5,10,0,0,322,323,
        5,23,0,0,323,324,3,32,16,0,324,325,5,24,0,0,325,327,1,0,0,0,326,
        304,1,0,0,0,326,312,1,0,0,0,327,45,1,0,0,0,328,329,5,29,0,0,329,
        339,5,1,0,0,330,331,5,30,0,0,331,339,5,1,0,0,332,333,5,31,0,0,333,
        334,3,22,11,0,334,335,5,1,0,0,335,339,1,0,0,0,336,337,5,31,0,0,337,
        339,5,1,0,0,338,328,1,0,0,0,338,330,1,0,0,0,338,332,1,0,0,0,338,
        336,1,0,0,0,339,47,1,0,0,0,340,341,5,23,0,0,341,342,3,32,16,0,342,
        343,5,24,0,0,343,49,1,0,0,0,344,345,7,6,0,0,345,51,1,0,0,0,346,347,
        3,56,28,0,347,348,3,54,27,0,348,351,1,0,0,0,349,351,3,54,27,0,350,
        346,1,0,0,0,350,349,1,0,0,0,351,53,1,0,0,0,352,356,5,32,0,0,353,
        356,5,33,0,0,354,356,5,34,0,0,355,352,1,0,0,0,355,353,1,0,0,0,355,
        354,1,0,0,0,356,55,1,0,0,0,357,358,5,35,0,0,358,57,1,0,0,0,359,362,
        5,37,0,0,360,362,5,38,0,0,361,359,1,0,0,0,361,360,1,0,0,0,362,59,
        1,0,0,0,363,364,5,36,0,0,364,367,5,9,0,0,365,368,5,41,0,0,366,368,
        3,50,25,0,367,365,1,0,0,0,367,366,1,0,0,0,368,369,1,0,0,0,369,370,
        5,10,0,0,370,61,1,0,0,0,28,65,72,86,106,112,124,126,137,148,159,
        167,172,185,205,211,217,225,235,248,280,302,319,326,338,350,355,
        361,367
    ]

class CGrammarParser ( Parser ):

    grammarFileName = "CGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'+'", "'-'", "'*'", "'&'", "'!'", 
                     "'++'", "'--'", "'('", "')'", "'/'", "'%'", "'<'", 
                     "'>'", "'=='", "'<='", "'>='", "'!='", "'&&'", "'||'", 
                     "'='", "','", "'{'", "'}'", "'if'", "'else'", "'while'", 
                     "'for'", "'break'", "'continue'", "'return'", "'int'", 
                     "'float'", "'char'", "'const'", "'printf'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'#include <stdio.h>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BLOCKCOMMENT", "SINGLE_LINE_COMMENT", 
                      "INT", "FLOAT", "IDENTIFIER", "CHAR", "IO", "WS" ]

    RULE_prog = 0
    RULE_instr = 1
    RULE_unary_operator = 2
    RULE_post_unary_operator = 3
    RULE_function_call = 4
    RULE_parenthesis_expression = 5
    RULE_unary_expression = 6
    RULE_mul_div_expression = 7
    RULE_add_sub_expression = 8
    RULE_relational_expression = 9
    RULE_logical_expression = 10
    RULE_assignment_expression = 11
    RULE_pointer = 12
    RULE_declaration_specification = 13
    RULE_declaration = 14
    RULE_expr = 15
    RULE_expr_loop = 16
    RULE_argumentlist = 17
    RULE_identifierlist = 18
    RULE_parameterlist = 19
    RULE_function = 20
    RULE_conditional_statement = 21
    RULE_loops = 22
    RULE_jumps = 23
    RULE_scope = 24
    RULE_constant = 25
    RULE_type = 26
    RULE_type_specifier = 27
    RULE_reserved_word = 28
    RULE_comment = 29
    RULE_printf = 30

    ruleNames =  [ "prog", "instr", "unary_operator", "post_unary_operator", 
                   "function_call", "parenthesis_expression", "unary_expression", 
                   "mul_div_expression", "add_sub_expression", "relational_expression", 
                   "logical_expression", "assignment_expression", "pointer", 
                   "declaration_specification", "declaration", "expr", "expr_loop", 
                   "argumentlist", "identifierlist", "parameterlist", "function", 
                   "conditional_statement", "loops", "jumps", "scope", "constant", 
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
    T__34=35
    T__35=36
    BLOCKCOMMENT=37
    SINGLE_LINE_COMMENT=38
    INT=39
    FLOAT=40
    IDENTIFIER=41
    CHAR=42
    IO=43
    WS=44

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
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.instr()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 17592093770366) != 0)):
                    break

            self.state = 67
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
            self.stdio = None # Token

        def expr(self):
            return self.getTypedRuleContext(CGrammarParser.ExprContext,0)


        def IO(self):
            return self.getToken(CGrammarParser.IO, 0)

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
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 6, 9, 23, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.expr(0)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                localctx.stdio = self.match(CGrammarParser.IO)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
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
            self.state = 74
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
            self.state = 76
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


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.iden = None # Token
            self.func = None # Token
            self.args = None # ArgumentlistContext

        def IDENTIFIER(self):
            return self.getToken(CGrammarParser.IDENTIFIER, 0)

        def argumentlist(self):
            return self.getTypedRuleContext(CGrammarParser.ArgumentlistContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = CGrammarParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function_call)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                self.state = 79
                localctx.func = self.match(CGrammarParser.T__8)
                self.state = 80
                self.match(CGrammarParser.T__9)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                self.state = 82
                localctx.func = self.match(CGrammarParser.T__8)
                self.state = 83
                localctx.args = self.argumentlist()
                self.state = 84
                self.match(CGrammarParser.T__9)
                pass


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
        self.enterRule(localctx, 10, self.RULE_parenthesis_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(CGrammarParser.T__8)
            self.state = 89
            self.assignment_expression()
            self.state = 90
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
            self.call = None # Function_callContext

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


        def function_call(self):
            return self.getTypedRuleContext(CGrammarParser.Function_callContext,0)


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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_unary_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 93
                self.unary_operator()
                self.state = 94
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 96
                self.unary_operator()
                self.state = 97
                self.constant()
                pass

            elif la_ == 3:
                self.state = 99
                self.constant()
                pass

            elif la_ == 4:
                self.state = 100
                self.parenthesis_expression()
                pass

            elif la_ == 5:
                self.state = 101
                localctx.iden = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 6:
                self.state = 102
                self.unary_operator()
                self.state = 103
                self.unary_expression(3)
                pass

            elif la_ == 7:
                self.state = 105
                localctx.call = self.function_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Unary_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unary_expression)
                    self.state = 108
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 109
                    self.post_unary_operator() 
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_mul_div_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.unary_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 124
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 118
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 119
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6160) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 120
                        self.unary_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = CGrammarParser.Mul_div_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mul_div_expression)
                        self.state = 121
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 122
                        self.match(CGrammarParser.T__11)
                        self.state = 123
                        self.unary_expression(0)
                        pass

             
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_add_sub_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.mul_div_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Add_sub_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expression)
                    self.state = 132
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 133
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==2 or _la==3):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 134
                    self.mul_div_expression(0) 
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_relational_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.add_sub_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Relational_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
                    self.state = 143
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 144
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 145
                    self.add_sub_expression(0) 
                self.state = 150
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_logical_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.relational_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 154
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 155
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==20):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 156
                    self.relational_expression(0) 
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
            self.lvalue = None # Declaration_specificationContext
            self.assign = None # Token
            self.rvalue = None # Assignment_expressionContext

        def logical_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Logical_expressionContext,0)


        def declaration_specification(self):
            return self.getTypedRuleContext(CGrammarParser.Declaration_specificationContext,0)


        def assignment_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Assignment_expressionContext,0)


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
        self.enterRule(localctx, 22, self.RULE_assignment_expression)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.logical_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                localctx.lvalue = self.declaration_specification()
                self.state = 164
                localctx.assign = self.match(CGrammarParser.T__20)
                self.state = 165
                localctx.rvalue = self.assignment_expression()
                pass


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
        self.enterRule(localctx, 24, self.RULE_pointer)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(CGrammarParser.T__3)
                self.state = 170
                self.pointer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(CGrammarParser.T__3)
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
        self.enterRule(localctx, 26, self.RULE_declaration_specification)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                localctx.typ = self.type_()
                self.state = 175
                localctx.ptr = self.pointer()
                self.state = 176
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                localctx.typ = self.type_()
                self.state = 179
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                localctx.var = self.match(CGrammarParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                localctx.ptr = self.pointer()
                self.state = 183
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

        def declaration_specification(self):
            return self.getTypedRuleContext(CGrammarParser.Declaration_specificationContext,0)


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
        self.enterRule(localctx, 28, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            localctx.lvalue = self.declaration_specification()
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


        def function(self):
            return self.getTypedRuleContext(CGrammarParser.FunctionContext,0)


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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 190
                self.assignment_expression()
                self.state = 191
                self.match(CGrammarParser.T__0)
                pass

            elif la_ == 2:
                self.state = 193
                self.declaration()
                self.state = 194
                self.match(CGrammarParser.T__0)
                pass

            elif la_ == 3:
                self.state = 196
                self.conditional_statement()
                pass

            elif la_ == 4:
                self.state = 197
                self.loops()
                pass

            elif la_ == 5:
                self.state = 198
                self.scope()
                pass

            elif la_ == 6:
                self.state = 199
                self.printf()
                self.state = 200
                self.match(CGrammarParser.T__0)
                pass

            elif la_ == 7:
                self.state = 202
                self.comment()
                pass

            elif la_ == 8:
                self.state = 203
                self.jumps()
                pass

            elif la_ == 9:
                self.state = 204
                self.function()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 207
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 208
                    self.comment() 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_expr_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8796000748156) != 0):
                self.state = 214
                self.expr(0)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ass = None # Assignment_expressionContext
            self.args = None # ArgumentlistContext

        def assignment_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Assignment_expressionContext,0)


        def argumentlist(self):
            return self.getTypedRuleContext(CGrammarParser.ArgumentlistContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_argumentlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentlist" ):
                listener.enterArgumentlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentlist" ):
                listener.exitArgumentlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentlist" ):
                return visitor.visitArgumentlist(self)
            else:
                return visitor.visitChildren(self)




    def argumentlist(self):

        localctx = CGrammarParser.ArgumentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_argumentlist)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                localctx.ass = self.assignment_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                localctx.ass = self.assignment_expression()
                self.state = 222
                self.match(CGrammarParser.T__21)
                self.state = 223
                localctx.args = self.argumentlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CGrammarParser.IDENTIFIER, 0)

        def identifierlist(self):
            return self.getTypedRuleContext(CGrammarParser.IdentifierlistContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_identifierlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierlist" ):
                listener.enterIdentifierlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierlist" ):
                listener.exitIdentifierlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierlist" ):
                return visitor.visitIdentifierlist(self)
            else:
                return visitor.visitChildren(self)



    def identifierlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CGrammarParser.IdentifierlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_identifierlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(CGrammarParser.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CGrammarParser.IdentifierlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_identifierlist)
                    self.state = 230
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 231
                    self.match(CGrammarParser.T__21)
                    self.state = 232
                    self.match(CGrammarParser.IDENTIFIER) 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParameterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.typ = None # TypeContext
            self.decl = None # DeclarationContext
            self.param = None # ParameterlistContext

        def type_(self):
            return self.getTypedRuleContext(CGrammarParser.TypeContext,0)


        def declaration(self):
            return self.getTypedRuleContext(CGrammarParser.DeclarationContext,0)


        def parameterlist(self):
            return self.getTypedRuleContext(CGrammarParser.ParameterlistContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_parameterlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterlist" ):
                listener.enterParameterlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterlist" ):
                listener.exitParameterlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterlist" ):
                return visitor.visitParameterlist(self)
            else:
                return visitor.visitChildren(self)




    def parameterlist(self):

        localctx = CGrammarParser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parameterlist)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                localctx.typ = self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                localctx.decl = self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                localctx.typ = self.type_()
                self.state = 241
                self.match(CGrammarParser.T__21)
                self.state = 242
                localctx.param = self.parameterlist()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                localctx.decl = self.declaration()
                self.state = 245
                self.match(CGrammarParser.T__21)
                self.state = 246
                localctx.param = self.parameterlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.returntype = None # Type_specifierContext
            self.funcname = None # Token
            self.param = None # ParameterlistContext
            self.funcbody = None # Expr_loopContext

        def type_specifier(self):
            return self.getTypedRuleContext(CGrammarParser.Type_specifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(CGrammarParser.IDENTIFIER, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(CGrammarParser.ParameterlistContext,0)


        def expr_loop(self):
            return self.getTypedRuleContext(CGrammarParser.Expr_loopContext,0)


        def getRuleIndex(self):
            return CGrammarParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = CGrammarParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_function)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                localctx.returntype = self.type_specifier()
                self.state = 251
                localctx.funcname = self.match(CGrammarParser.IDENTIFIER)
                self.state = 252
                self.match(CGrammarParser.T__8)
                self.state = 253
                localctx.param = self.parameterlist()
                self.state = 254
                self.match(CGrammarParser.T__9)
                self.state = 255
                self.match(CGrammarParser.T__22)
                self.state = 256
                localctx.funcbody = self.expr_loop()
                self.state = 257
                self.match(CGrammarParser.T__23)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                localctx.returntype = self.type_specifier()
                self.state = 260
                localctx.funcname = self.match(CGrammarParser.IDENTIFIER)
                self.state = 261
                self.match(CGrammarParser.T__8)
                self.state = 262
                localctx.param = self.parameterlist()
                self.state = 263
                self.match(CGrammarParser.T__9)
                self.state = 264
                self.match(CGrammarParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                localctx.returntype = self.type_specifier()
                self.state = 267
                localctx.funcname = self.match(CGrammarParser.IDENTIFIER)
                self.state = 268
                self.match(CGrammarParser.T__8)
                self.state = 269
                self.match(CGrammarParser.T__9)
                self.state = 270
                self.match(CGrammarParser.T__22)
                self.state = 271
                localctx.funcbody = self.expr_loop()
                self.state = 272
                self.match(CGrammarParser.T__23)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 274
                localctx.returntype = self.type_specifier()
                self.state = 275
                localctx.funcname = self.match(CGrammarParser.IDENTIFIER)
                self.state = 276
                self.match(CGrammarParser.T__8)
                self.state = 277
                self.match(CGrammarParser.T__9)
                self.state = 278
                self.match(CGrammarParser.T__0)
                pass


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
        self.enterRule(localctx, 42, self.RULE_conditional_statement)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(CGrammarParser.T__24)
                self.state = 283
                self.match(CGrammarParser.T__8)
                self.state = 284
                localctx.condition = self.assignment_expression()
                self.state = 285
                self.match(CGrammarParser.T__9)
                self.state = 286
                self.match(CGrammarParser.T__22)
                self.state = 287
                localctx.ifbody = self.expr_loop()
                self.state = 288
                self.match(CGrammarParser.T__23)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.match(CGrammarParser.T__24)
                self.state = 291
                self.match(CGrammarParser.T__8)
                self.state = 292
                localctx.condition = self.assignment_expression()
                self.state = 293
                self.match(CGrammarParser.T__9)
                self.state = 294
                self.match(CGrammarParser.T__22)
                self.state = 295
                localctx.ifbody = self.expr_loop()
                self.state = 296
                self.match(CGrammarParser.T__23)
                self.state = 297
                self.match(CGrammarParser.T__25)
                self.state = 298
                self.match(CGrammarParser.T__22)
                self.state = 299
                localctx.elsebody = self.expr_loop()
                self.state = 300
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
        self.enterRule(localctx, 44, self.RULE_loops)
        self._la = 0 # Token type
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                localctx.loop = self.match(CGrammarParser.T__26)
                self.state = 305
                self.match(CGrammarParser.T__8)
                self.state = 306
                localctx.condition = self.assignment_expression()
                self.state = 307
                self.match(CGrammarParser.T__9)
                self.state = 308
                self.match(CGrammarParser.T__22)
                self.state = 309
                localctx.body = self.expr_loop()
                self.state = 310
                self.match(CGrammarParser.T__23)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                localctx.loop = self.match(CGrammarParser.T__27)
                self.state = 313
                self.match(CGrammarParser.T__8)
                self.state = 314
                localctx.before = self.declaration()
                self.state = 315
                self.match(CGrammarParser.T__0)
                self.state = 316
                localctx.condition = self.assignment_expression()
                self.state = 317
                self.match(CGrammarParser.T__0)
                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8310761718396) != 0):
                    self.state = 318
                    localctx.after = self.assignment_expression()


                self.state = 321
                self.match(CGrammarParser.T__9)
                self.state = 322
                self.match(CGrammarParser.T__22)
                self.state = 323
                localctx.body = self.expr_loop()
                self.state = 324
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
            self.beforereturn = None # Assignment_expressionContext

        def assignment_expression(self):
            return self.getTypedRuleContext(CGrammarParser.Assignment_expressionContext,0)


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
        self.enterRule(localctx, 46, self.RULE_jumps)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                localctx.jump = self.match(CGrammarParser.T__28)
                self.state = 329
                self.match(CGrammarParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                localctx.jump = self.match(CGrammarParser.T__29)
                self.state = 331
                self.match(CGrammarParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 332
                localctx.jump = self.match(CGrammarParser.T__30)
                self.state = 333
                localctx.beforereturn = self.assignment_expression()
                self.state = 334
                self.match(CGrammarParser.T__0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 336
                localctx.jump = self.match(CGrammarParser.T__30)
                self.state = 337
                self.match(CGrammarParser.T__0)
                pass


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

        def expr_loop(self):
            return self.getTypedRuleContext(CGrammarParser.Expr_loopContext,0)


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
        self.enterRule(localctx, 48, self.RULE_scope)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            localctx.startscope = self.match(CGrammarParser.T__22)
            self.state = 341
            self.expr_loop()
            self.state = 342
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
        self.enterRule(localctx, 50, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6047313952768) != 0)):
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
        self.enterRule(localctx, 52, self.RULE_type)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.reserved_word()
                self.state = 347
                self.type_specifier()
                pass
            elif token in [32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
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
        self.enterRule(localctx, 54, self.RULE_type_specifier)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                localctx.typ = self.match(CGrammarParser.T__31)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                localctx.typ = self.match(CGrammarParser.T__32)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                localctx.typ = self.match(CGrammarParser.T__33)
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
        self.enterRule(localctx, 56, self.RULE_reserved_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(CGrammarParser.T__34)
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
        self.enterRule(localctx, 58, self.RULE_comment)
        try:
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                localctx.block = self.match(CGrammarParser.BLOCKCOMMENT)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
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
        self.enterRule(localctx, 60, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(CGrammarParser.T__35)
            self.state = 364
            self.match(CGrammarParser.T__8)
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.state = 365
                self.match(CGrammarParser.IDENTIFIER)
                pass
            elif token in [39, 40, 42]:
                self.state = 366
                self.constant()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 369
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
        self._predicates[6] = self.unary_expression_sempred
        self._predicates[7] = self.mul_div_expression_sempred
        self._predicates[8] = self.add_sub_expression_sempred
        self._predicates[9] = self.relational_expression_sempred
        self._predicates[10] = self.logical_expression_sempred
        self._predicates[15] = self.expr_sempred
        self._predicates[18] = self.identifierlist_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def unary_expression_sempred(self, localctx:Unary_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

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
                return self.precpred(self._ctx, 4)
         

    def identifierlist_sempred(self, localctx:IdentifierlistContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         




