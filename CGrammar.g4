grammar CGrammar;

prog: instr+ EOF
	;

instr: expr ';'
	;

expr:   expr (MULTIPLICATION|DIVISION) expr
	|	expr (ADDITION|SUBTRACTION) expr
	|	expr ('=='|'>'|'<') expr
	|	expr ('%') expr
	|   UNARY_OPERATOR expr
	|	expr ('&&' | '||') expr
	|	('!') expr
	|	expr ('>=' | '<=' | '!=') expr
	|	INT
	|	'(' expr ')'
	;

UNARY_OPERATOR:  '+'
    |   '-'
    ;
MULTIPLICATION: '*';
DIVISION:   '/';
ADDITION:   '+';
SUBTRACTION:    '-';
INT: [0-9]+;
WS: [ \n\t\r]+ -> skip;