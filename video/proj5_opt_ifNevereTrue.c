#include <stdio.h>

int main() {

    if(1==2 || 0){
        printf("Never True");
    }
    else{
        if(0){
            printf("Never True");
        }
        else{
            printf("Always True");
        }
    }
    return 1;
}
