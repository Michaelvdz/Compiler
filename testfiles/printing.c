/*
* Printing operations
*/

int y1 = 1;
printf(y1);
int* ptr = &y1;
*ptr = 2;
printf(y1); // Should output the value of y1 which sould be 2
int* ptr2 = &y1;
ptr2 = &y1;
*ptr2 = 3;
printf(y1); // Should output the value of y1 which should be 3

char x = 'x';
char* char_pointer = &x;
*char_pointer = 'H';
printf(x); // Printing H

char y = 'x';
char_pointer = &y;
*char_pointer = 'e';
printf(y); // Printing e

*char_pointer = 'l';
printf(y); // Printing l
printf(y); // Printing l

*char_pointer = 'o';
printf(y); // Printing o

printf('3');
printf(21);
