//my_strindex.c

#include "../lib/my.h"

char*	my_strindex(char* original, char find)
{
	if(original!=NULL)
		for(;*original != '\0'; original++)
			if(*original == find)
				return original;
				
	return NULL;
}
