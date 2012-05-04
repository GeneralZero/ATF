//my_digits.c

#include "../lib/my.h"

void my_digits()
{
	char start;

	for(start = '0'; start <='9'; start++)
	{
		my_char(start);
	}
	my_char('\n');
}
