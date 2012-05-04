//my_strcat.c

#include "../lib/my.h"

char*	my_strcat(char* dest, char* src)
{
	//char* ret;
	if(dest==NULL && src==NULL)
		return NULL;
	else if(dest==NULL)
		return dest;
	if(src==NULL)
		return dest;
	else
	{
		int length = my_strlen(dest);
		int count=0;
		//for(count=0; dest[count]; count++)
		//	ret[count] = dest[count];
		for(count=0; src[count]!='\0'; count++)
			dest[length+count] = src[count];
		dest[count+length] = '\0';
	}
	return dest;
}
