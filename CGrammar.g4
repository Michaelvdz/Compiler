grammar CGrammar;

prog: instr+ EOF
	;

instr: expr ';'
    | comment
    | printf ';'
	;

unary_operator:  '+'
    |   '-'
    |   '*'
    |   '&'
    |   '!'
    ;
parenthesis_expression: '(' expr ')'
    ;

unary_expression:   unary_operator iden=IDENTIFIER
    |   unary_operator constant
    |   constant
    |   parenthesis_expression
    |   iden=IDENTIFIER
    |   unary_operator unary_expression
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

declaration_specification:  type '*' var=IDENTIFIER
    | type var=IDENTIFIER
    | var=IDENTIFIER
    ;

declaration:    lvalue=declaration_specification assign='=' rvalue=assignment_expression
    | lvalue=declaration_specification
    ;

expr:   assignment_expression
    | declaration
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
    |   sl=SINGLE_LINE_COMMMENT
    ;

printf: 'printf' '(' (IDENTIFIER | constant) ')'
    ;

BLOCKCOMMENT: '/*' .*? '*/';
SINGLE_LINE_COMMMENT: '//'~( '\r' | '\n' )*;
INT: [0-9]+;
FLOAT: [0-9]*? '.' [0-9]+;
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;
CHAR: ['] . ['];
WS: [ \n\t\r]+ -> skip;