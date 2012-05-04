//str2vect.c

#include "../lib/my.h"

char**	str2vect(char* string)
{
	int i = 0; 	// counter
	char flag;	// flag to test if changing from spaces to a string
	int s = 0;	// count for number of strings
	int w; 		// word counter
	int end;
	
	for(; *(string) == ' ' || *(string) == '\t'; string++);
	
	//my_str(string);
	
	for(s=1, i=0, flag=1; string[i]!='\0'; i++)
	{
		if(string[i] == ' ' || string[i] == '\t')
			if(flag==1)
				flag=0;
		
		else if(string[i] != ' ' && string[i] != '\t')
			//my_char(string[i]);
			if(flag==0)
			{
				flag=1;
				s++;
			}
	}
	/*
	my_str("Number of Words:");
	my_int(s);
	*/
	
	char** ret = (char**)my_xmalloc((w+1)*sizeof(char*));
	string = my_strdup(test);
	
	for(w=0,s=0,i=0, flag=1; string[i]!='\0'; i++)
	{
		if(string[i] == ' ' || string[i] == '\t')
			if(flag==1)
			{
				flag=0;
				ret[s] = (char*)my_xmalloc(sizeof(char)*(w+1));
				ret[s++] = my_strncat(string[end],"\0", w+1);
			}
		
		else if(string[i] != ' ' && string[i] != '\t')
			//my_char(string[i]);
			w++;
			if(flag==0)
			{
				flag=1;
				s=0;
				end = i;
			}
	}
	
}
	
int main()
{
	str2vect("Hello \t      World    \t     !   \t");
}
