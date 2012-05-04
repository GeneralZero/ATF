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
		//my_char(string[i]);
		if(string[i] == ' ' || string[i] == '\t')
		{
			if(flag==1)
				flag=0;
		}
		else if(string[i] != ' ' && string[i] != '\t')
		{	
			//my_char(string[i]);
			if(flag==0)
			{
				flag=1;
				s++;
			}
		}
	}

	my_str("Number of Words:");
	my_int(s);

	
	char** ret = (char**)my_xmalloc((s+1)*sizeof(char*));
	//string = my_strdup(test);
	
	for(end=0, w=0, s=0, i=0, flag=1; string[i]!='\0'; i++)
	{
		if(string[i] == ' ' || string[i] == '\t')
		{
			if(flag==1)
			{
				flag=0;
				//s++;
				//my_int(w);
				ret[s] = (char*)my_xmalloc(sizeof(char)*(w+1));
				ret[s++] = my_strnconcat(&string[end],"\0", w);
				//my_str(&(string[end]));
			}
		}
		else if(string[i] != ' ' && string[i] != '\t')
		{
			//my_char(string[i]);
			if(flag==0)
			{
				flag=1;
				w=0;
				end = i;
				my_int(w);
				//my_int(i);
			}
			w++;
		}
	}
	ret[s] = NULL;
	return ret;
}
	
int main()
{
	char** testing;
	int i;

	testing = str2vect("   \t  Hello \t      World    \t     !   \t");
	
	for(i=0; testing[i]!=NULL; i++)
	{
		my_str(testing[i]);
		my_char('|');
	}
}
