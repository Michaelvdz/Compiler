#include <stdio.h>

//should generate -1;

int main() {
int number = -55;

number++;

number = number++;


int n = number++;


n = n - n++;
printf("%d;",n);
return 0;
}
