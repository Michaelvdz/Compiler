#include <stdio.h>

// Should generate warning
// Should print 0, 0, B
int main(){
    float x = 0.5;
    int y = x;
    int z = 0.5;
    printf("%d, ", y);
    printf("%d, ", z);

    int a = 66;
    char b = a;
    printf("%c", b);
    return 1;
}
