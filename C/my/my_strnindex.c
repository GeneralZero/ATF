//my_strnindex.c

#include "../lib/my.h"

char*	my_strnindex(char* original, char find, int length)
{
	if(original!=NULL)
		for(;*original != '\0' && length>0; original++, length--)
			if(*original == find)
				return original;
				
	return NULL;
}
