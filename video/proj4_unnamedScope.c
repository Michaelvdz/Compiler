#include <stdio.h>
//Should print 0, 1, 1, 0
int main() {
    {
        int x  = 0;
        printf("%d,", x);
        {
            int x = 1;
            printf("%d,", x);
            {
                printf("%d,", x);
            }
        }
        {
            printf("%d", x);
        }
    }
return 0;
}
