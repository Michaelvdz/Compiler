grammar CGrammar;

prog: instr+ EOF
	;

instr: expr
    | stdio=IO
    | ';'+
	;

unary_operator:  '+'
    |   '-'
    |   '*'
    |   '&'
    |   '!'
    |   '++'
    |   '--'
    ;

post_unary_operator:  '++'
    |   '--'
    |   '[' ass=assignment_expression ']'
    ;

function_call:
    iden=IDENTIFIER func='(' ')'
    | iden=IDENTIFIER func='(' args=argumentlist ')'
    ;

parenthesis_expression: '(' assignment_expression ')'
    ;

unary_expression:   unary_operator iden=IDENTIFIER
    |   unary_operator constant
    |   constant
    |   parenthesis_expression
    |   iden=IDENTIFIER
    |   unary_operator unary_expression
    |   unary_expression post_unary_operator
    |   call=function_call
    ;

mul_div_expression: mul_div_expression op=('*'|'/'|'%') unary_expression
    |   mul_div_expression '%' unary_expression
    |   unary_expression
    ;
add_sub_expression: add_sub_expression op=('+'|'-') mul_div_expression
    |   mul_div_expression
    ;

relational_expression:  relational_expression op=('<'|'>'|'=='|'<='|'>='|'!=') add_sub_expression
    |   add_sub_expression
    ;

logical_expression:  logical_expression op=('&&'|'||') relational_expression
    |   relational_expression
    ;

assignment_expression:  logical_expression
    | lvalue=declaration_specification assign='=' rvalue=assignment_expression
    ;

pointer:    star='*' ptr=pointer
    | star='*'
    ;

declaration_specification:  typ=type ptr=pointer var=IDENTIFIER
    | typ=type var=IDENTIFIER
    | var=IDENTIFIER
    | ptr=pointer var=IDENTIFIER
    | typ=type ptr=pointer var=IDENTIFIER arr=array
    | typ=type var=IDENTIFIER arr=array
    | var=IDENTIFIER arr=array
    | ptr=pointer var=IDENTIFIER arr=array
    ;

array:
    '[' ']'
    | '[' assignment_expression ']'
    ;

declaration:
    lvalue=declaration_specification
    ;

expr:   assignment_expression ';'+
    | declaration ';'+
    | conditional_statement
    | loops
    | scope
    | printf ';'+
    | comment
    | jumps
    | function
    | scanf ';'+
	;

expr_loop:
    expr*
    ;

argumentlist:
    ass=assignment_expression
    | ass=assignment_expression  ',' args=argumentlist
    ;

parameterlist:
    typ=type
    | decl=declaration
    | typ=type ',' param=parameterlist
    | decl=declaration ',' param=parameterlist
    ;

function:
    returntype=type_specifier funcname=IDENTIFIER '(' param=parameterlist ')' body='{' funcbody=expr_loop '}'
    | returntype=type_specifier funcname=IDENTIFIER '(' param=parameterlist ')' ';'
    | returntype=type_specifier funcname=IDENTIFIER '(' ')' body='{' funcbody=expr_loop '}'
    | returntype=type_specifier funcname=IDENTIFIER '(' ')' ';'
    ;

conditional_statement:
    'if' '(' condition=assignment_expression ')' '{' ifbody=expr_loop '}'
    | 'if' '(' condition=assignment_expression ')' '{' ifbody=expr_loop '}' 'else' '{' elsebody=expr_loop '}'
    | 'switch' '(' assignment_expression ')' '{' case* '}'
    ;

case:
    'case' logical_expression ':' expr_loop
    | 'default' ':' expr_loop
    ;

loops:
    loop='while' '(' condition=assignment_expression ')' '{' body=expr_loop '}'
    | loop='for' '(' before=assignment_expression ';' condition=assignment_expression ';' after=assignment_expression? ')' '{' body=expr_loop '}'
    ;

jumps:
    jump='break' ';'
    | jump='continue' ';'
    | jump='return' beforereturn=assignment_expression ';'
    | jump='return' ';'
    ;

scope:
    startscope='{' expr_loop endscope='}'
    ;

constant:   INT
    | FLOAT
    | CHAR
    ;

type:   reserved_word type_specifier
    | type_specifier
    ;

type_specifier: typ='int'
    |   typ='float'
    |   typ='char'
    |   typ='void'
   ;

reserved_word:  'const'
    ;

comment: block=BLOCKCOMMENT
    |   sl=SINGLE_LINE_COMMENT
    ;

printfArgslist:
    ass=assignment_expression
    | string=FORMAT
    | ass=assignment_expression  ',' args=printfArgslist
    | string=FORMAT ',' args=printfArgslist
    ;

printf:
    'printf' '(' form=FORMAT ',' args=printfArgslist ')'
    | 'printf' '(' form=FORMAT ')'
    ;

scanf:
    'scanf' '(' form=FORMAT ',' args=printfArgslist ')'
    | 'scanf' '(' form=FORMAT ')'
    ;

BLOCKCOMMENT: '/*' .*? '*/';
SINGLE_LINE_COMMENT: '//'~( '\r' | '\n' )*;
INT: ([1-9][0-9]*|[0]);
FLOAT: [0-9]*? '.' [0-9]+;
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;
FORMAT: ["](.)*?["];
CHAR: (['].[']|['][\\].[']);
IO: '#include <'(.)*?'.h>';
WS: [ \n\t\r]+ -> skip;