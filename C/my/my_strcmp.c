//my_strcmp.c

#include "../lib/my.h"

int		my_strcmp(char* dest, char* src)
{
	int count;
	if(dest==NULL && src== NULL)
		return 0;
	else if(dest==NULL)
		return -1;
	else if(src==NULL)
		return 1;
	else
	{
		for(count=0; dest[count]!='\0' && src[count]!='\0'; count++)
			if(dest[count]!=src[count])
				return (int)(dest[count] - src[count]);
		
		return 0;
	}
}
