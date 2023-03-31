/*
* Comparison operations
*/

int x = 1>= 0; // Should be 1
x = 1>=-1; // Should be 1
x = 1<=0; // Should be 0
x = 1<=1; // Should be 1
x = 1<=2; // Should be 1
x = 1!=0; // Should be 1
x = 1!=(2-1); // Should be 0