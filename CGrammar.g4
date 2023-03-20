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

unary_expression:   unary_operator IDENTIFIER
    |   unary_operator constant
    |   constant
    |   parenthesis_expression
    |   IDENTIFIER
    ;

mul_div_expression: mul_div_expression op=('*'|'/') unary_expression
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

declaration_specification:  type '*' IDENTIFIER
    | type IDENTIFIER
    | IDENTIFIER
    ;

declaration:    declaration_specification '=' assignment_expression
    | declaration_specification
    ;

expr:   assignment_expression
    | declaration
	;



constant:   INT
    | FLOAT
    | CHAR
    ;

type:   reserved_word type
    |   'int'
    |   'float'
    |   'char'
    ;

reserved_word:  'const'
    ;

comment: BLOCKCOMMENT
    |   SINGLE_LINE_COMMMENT
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