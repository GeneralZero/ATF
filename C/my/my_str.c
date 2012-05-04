//my_str.c

#include "../lib/my.h"

void my_str(char* string)
{
	if(string != NULL){
		int i;
		for(i=0;string[i]!='\0';i++)
			my_char(string[i]);
		//my_char('\n');
	}
}
		
