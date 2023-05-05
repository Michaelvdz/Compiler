#include <stdio.h>

int x = 1;
float y = 3.0;
int z = 4;

//should print 1, 2, 3
void func(){
    int z = 2;
    printf("%d,", x);
    printf("%d,", z);
}

int main(){
    func();
    printf("%f", y);
    return 0;
}