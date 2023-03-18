grammar CGrammar;

prog: instr+ EOF
	;

instr: expr ';'
	;

unary_operator:  '+'
    |   '-'
    ;
parenthesis_expression: '(' expr ')'
    ;

unary_expression:   unary_operator constant
    |   constant
    |   parenthesis_expression
    ;

mul_div_expression: mul_div_expression op=('*'|'/') unary_expression
    |   mul_div_expression ('%') unary_expression
    |   unary_expression
    ;
add_sub_expression: add_sub_expression op=('+'|'-') mul_div_expression
    |   mul_div_expression
    ;

relational_expression:  relational_expression op=('<'|'>'|'=='|'<='|'>='|'!=') add_sub_expression
    |   add_sub_expression
    ;

logical_expression:  logical_expression op=('&&'|'||') logical_expression
    |   '!' logical_expression
    |   constant
    ;


expr:   relational_expression
	;

constant:   INT
    ;

INT: [0-9]+;
WS: [ \n\t\r]+ -> skip;