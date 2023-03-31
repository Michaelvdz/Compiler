/*
* Modulo operations
*/

int x = 9%3; // Should be 0
x = 9%8; // Should be 1
x = 9%0; // Should be NaN and throw warning
x = 9%1; // Should be 0
x = 9%(1+1); // Should be 1
x = 9%(5+1); // Should be 3