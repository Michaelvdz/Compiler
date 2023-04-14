grammar CGrammar;

prog: instr+ EOF
	;

instr: expr
	;

unary_operator:  '+'
    |   '-'
    |   '*'
    |   '&'
    |   '!'
    ;

post_unary_operator:  '++'
    |   '--'
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
    ;

pointer:    '*' pointer
    | '*'
    ;

declaration_specification:  typ=type ptr=pointer var=IDENTIFIER
    | typ=type var=IDENTIFIER
    | var=IDENTIFIER
    | ptr=pointer var=IDENTIFIER
    ;

declaration:    lvalue=declaration_specification assign='=' rvalue=assignment_expression
    | lvalue=declaration_specification
    ;

expr:   assignment_expression ';'
    | declaration ';'
    | conditional_statement
    | loops
    | scope
    | printf ';'
    | expr comment
    | comment
    | jumps
	;

expr_loop:
    expr*
    ;

conditional_statement:
    'if' '(' condition=assignment_expression ')' '{' ifbody=expr_loop '}'
    | 'if' '(' condition=assignment_expression ')' '{' ifbody=expr_loop '}' 'else' '{' elsebody=expr_loop '}'
    ;

loops:
    loop='while' '(' condition=assignment_expression ')' '{' body=expr_loop '}'
    | loop='for' '(' before=declaration ';' condition=assignment_expression ';' after=assignment_expression? ')' '{' body=expr_loop '}'
    ;

jumps:
    jump='break' ';'
    | jump='continue' ';'
    ;

scope:
    startscope='{' expr* endscope='}'
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
   ;

reserved_word:  'const'
    ;

comment: block=BLOCKCOMMENT
    |   sl=SINGLE_LINE_COMMENT
    ;

printf: 'printf' '(' (IDENTIFIER | constant) ')'
    ;

BLOCKCOMMENT: '/*' .*? '*/';
SINGLE_LINE_COMMENT: '//'~( '\r' | '\n' )*;
INT: [0-9]+;
FLOAT: [0-9]*? '.' [0-9]+;
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;
CHAR: ['] . ['];
WS: [ \n\t\r]+ -> skip;