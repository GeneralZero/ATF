//my_find.c

#include "../lib/my.h"

int my_find(char* string, char idx)
{	
	int i;
	if(string != NULL)
		for(i=0; string[i]!= '\0'; i++)
			if(string[i] == idx)
				//my_int(++count);
				return ++i;
	//my_int(count);
	return -1;
}
