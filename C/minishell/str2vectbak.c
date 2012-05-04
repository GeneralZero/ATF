//str2vect.c

#include "../lib/my.h"

char**	str2vect(char* test)
{
	int i = 0;
	char flag;// flag to test if changing from spaces to a string
	int s = 0;// count for
	
	for(; *(test) == ' ' || *(test) == '\t'; test++);
	
	char* string = (char*)my_xmalloc(my_strlen(test)*sizeof(char));
	string = my_strdup(test);
	
	for(i=0, flag=1; string[i]!='\0'; i++)
	{
		if((string[i] == ' ' || string[i] == '\t') && flag==1)
			flag=0;
		else if((string[i] != ' ' && string[i] != '\t') && flag==0)
		{
			flag=1;
			s++;
		}
	}
	
	char** ret = (char**)my_xmalloc(sizeof(char*)*s++);
	ret[0] = string;
	char* backtrack;
	//my_str(string);
	
	for(s=1, i=0, flag=1; string[i]!='\0'; i++)
	{
		//my_char(string[i]);
		if((string[i] == ' ' || string[i] == '\t') && flag==1)
		{	
			//my_char(string[i]);
			string[i] = '\0';
			flag=0;
		}
		else if((string[i] != ' ' && string[i] != '\t') && flag==0)
		{
			//my_char(string[i]);
			flag=1;
			ret[s++] = &string[i];
		}
	}
	ret[s] = NULL;
	
	/*
	for(i=0; ret[i]!=NULL; i++)
		my_str(ret[i]);
	*/
}
