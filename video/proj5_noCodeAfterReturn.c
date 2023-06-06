#include <stdio.h>

//Should print 0, 1, 3
int main() {
    int x = 0;
    int y = 1;
    float z = 3.0;
    char ch = 'x';
    printf("%d, ", x);
    printf("%d, ", y);
    printf("%f", z);
    return 0;
    //Should not print after return
    printf("%c", ch);
}
