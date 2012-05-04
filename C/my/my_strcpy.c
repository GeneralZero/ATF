//my_strcpy.c

#include "../lib/my.h"

char*	my_strcpy(char* dest, char* src)
{
	char* ret = dest;
	if(dest!=NULL && src !=NULL)
	{
		int count;
		ret =my_xmalloc(my_strlen(dest));
		for(count = 0; src[count]!='\0'; count++)
			ret[count] = src[count];
		ret[++count] = '\0';
	}
	return ret;
}
