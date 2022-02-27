#include <stdio.h>

int main()
{
	int a = 2;
	double d = 1.5;
	float pi = 22.0 / 7.0;
	char c = 'a';
	printf("Here i%c a %s: %d+%d = %d\n\n", 's', "Calculation", a, a, a + a);
	a = 5; // Chnage variable value
	printf("Here i%c a %s: %d+%d = %d\n", 's', "Calculation", a, a, a + a);
	// func();
	return (0);
}

int func()
{
	puts("Func Running");
}
