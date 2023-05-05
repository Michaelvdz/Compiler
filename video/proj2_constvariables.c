#include <stdio.h>

// Should print the numbers 5, 0.5 and the char c
// With constant propagation z = 15 and yy = 0.25
int main(){
    const int x = 5;
    const float y = 0.5;
    const char c = 'c';
    int z = x + 10;
    float yy = y*y;
    printf("%d; %f; %c", x, y, c);
}
