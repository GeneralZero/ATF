//my_rfind.c

#include "../lib/my.h"

int my_rfind(char* string, char idx)
{
	int ret =-1;
	if(string != NULL)
	{
		int count;
		for(count=0; string[count]!= '\0'; count++)
			if(string[count] == idx)
				ret = ++count;
		return ret;
	}
	//my_int(ret);
	return -1;
}

