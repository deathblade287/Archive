// #include <stdio.h>

// int main()
// {
// 	int c;

// 	printf("Type a letter: ");
// 	c = getchar();
// 	// printf("You typed '%c'.\n", c);
// 	printf("You typed '");
// 	putchar(c);
// 	printf("'.\n");

// 	return (0);
// }

#include <stdio.h>

int main()
{
	int a, b, c;

	printf("Type three letters: ");
	a = getchar();
	putchar(a);
	b = getchar();
	putchar(b);
	c = getchar();
	putchar(c);
	printf("\n");

	return (0);
}
