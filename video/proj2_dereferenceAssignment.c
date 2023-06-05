#include <stdio.h>

// This should print:
//  10, 10,
//  9, 9,
//  10.0, 10.0,
//  9.0, 9.0,
//  10, 10,
//  11, 11,
//  10.0, 10.0
//  11.0, 11.0

int main(){
	int x = 0;
	int* xp = &x;
	float y = 1.0;
	float* yp = &y;
	*xp = 10;
	printf("%d; ", x);
	printf("%d\n", *xp);
	(*xp)--;
	printf("%d; ", x);
	printf("%d\n", *xp);
	*yp = 10.0;
	printf("%f; ", y);
	printf("%f\n", *yp);
	(*yp)--;
	printf("%f; ", y);
	printf("%f\n", *yp);
	*xp = 10;
	printf("%d; ", x);
	printf("%d\n", *xp);
	(*xp)++;
	printf("%d; ", x);
	printf("%d\n", *xp);
	*yp = 10.0;
	printf("%f; ", y);
	printf("%f\n", *yp);
	(*yp)++;
	printf("%f; ", y);
	printf("%f\n", *yp);
	return 1;
}
