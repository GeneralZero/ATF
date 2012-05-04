//my_strncpy.c

#include "../lib/my.h"

char*	my_strncpy(char* dest, char* src, int size)
{
	int count=0;
	char* ret = NULL;
	if(dest==NULL)
		return NULL;
	if(src ==NULL)
	{
		//int length = my_strlen(src);
		ret = (char*)my_xmalloc(size*sizeof(char));
		for(count = 0; dest[count]!='\0' && count<size; count++)
			ret[count] = dest[count];
		if(count<size)
			ret[count++] = '\0';
		return ret;
	}
	else
	{
		//int length = my_strlen(src);
		ret = (char*)my_xmalloc(size*sizeof(char));
		for(count = 0; src[count]!='\0' && count<size; count++)
			ret[count] = src[count];
		if(count<size)
			ret[count++] = '\0';
		return ret;
	}
	return dest;
}
