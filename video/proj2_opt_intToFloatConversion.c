#include <stdio.h>

// Should NOT generate warning
// Should prnt 5; 1.5
int main(){
    int x = 5;
    float y = x;
    float z = 0.5 + 1;
    printf("%f, ", y);
    printf("%f", z);
    return 1;
}