//my_strncmp.c

#include "../lib/my.h"

int	my_strncmp(char* dest, char* src, int length)
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
		for(count=0; (dest[count]!='\0' && src[count]!='\0') && count<length; count++)
			if(dest[count]!=src[count])
				return (int)(dest[count] - src[count]);
		return 0;
	}
}
