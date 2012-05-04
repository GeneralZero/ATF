//my_digits2.c

#include "../lib/my.h"

char* my_digits2()
{
	char* ret = (char*)my_xmalloc(11*sizeof(char));
	char start;
	int i;

	for(i=0, start = '0'; start <='9'; start++)
	{
		ret[i++] = start;
	}
	ret[10] = '\0';
	
	return ret;
	//my_char('\n');
}
