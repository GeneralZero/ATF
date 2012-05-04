//my_revstr.c

#include "../lib/my.h"

int my_revstr(char* string)
{
	if(string != NULL)
	{
		int end;
		int start;
		char swap;
		for(start=0, end = my_strlen(string); start<end/2; start++)
		{
			swap = string[start];
			string[start] = string[end-1-start];
			string[end-1-start] = swap;			
		}
		//my_str(string);
		return end;
	}
}

