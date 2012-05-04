//my_strdup.c

#include "../lib/my.h"

char*	my_strdup(char* original)
{
	char* ret = NULL;
	if(original!=NULL)
	{
		int length = my_strlen(original); 
		ret = (char*)my_xmalloc(sizeof(char)*length);

		for(;length>=0; length--)
			ret[length] = original[length];
	}
	return ret;
}
