#include <stdio.h>

// This should print the number 10 for nested expressions
int main(){
        int x = 2;
        printf("%d; ", -x*-(2+3));
        printf("%d; ", +x*4+x);
        printf("%d; ", 10/2+10/x);
        printf("%d; ", ((100-80)/x)+(5-5));

        return 1;
}
