//my_alpha.c

#include "../lib/my.h"

void my_alpha()
{
	char start;
	for(start = 'a'; start <= 'z'; start++)
		my_char(start);
	my_char('\n');
}
