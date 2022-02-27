#include <stdio.h>
#include <math.h>

int main()
{
    float a;
    float b;
    printf("Value for a : ");
    scanf("%f", &a);
    printf("Value for b : ");
    scanf("%f", &b);

    // Adding The Values
    printf("\nAdding : %f\n\n", a + b);
    // Subtracting The Values
    printf("Subtracting : %f\n\n", a - b);
    // Multiplying The Values
    printf("Multiplying : %f\n\n", a * b);
    // Dividing The Values
    printf("Dividing : %f\n\n", a / b);
    // Setting A to Exponent B
    printf("Exponent : %f\n\n", pow(a, b));
    // Sqare Root Of Both The Values
    printf("Square Root : %f & %f\n\n", sqrt(a), sqrt(b));

    return (0);
}
