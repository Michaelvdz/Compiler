/*
* Logical operations
*/

int x = 1 && 1; // Should be 1
x = 1 && 0; // Should be 0
x = 1 || 0; // Should be 1
x = 0 || 0 ; // Should be 0
x = 1 || 1; // Should be 1
x = 0 || 1; // Should be 1
x = 5 && -5; // Should be 1
x = -0 && 1; // Should be 0
x = !( 0 && 0); // Should be 1
x = !( 5 && 5 || (0) ); // Should be 0