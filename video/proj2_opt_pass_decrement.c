#include <stdio.h>

int main() {
int x = 5;
x--;
printf("%d",x);
int z = x--;
printf("%d",z);
x = x-- + z--;
printf("%d",x);
return 0;
}
