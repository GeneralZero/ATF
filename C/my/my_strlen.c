//my_strlen.c

#include "../lib/my.h"

int my_strlen(char* string)
{
	int count = 0;
	if(string != NULL)
		for(;string[count] !='\0'; count++);
	return count;
}
