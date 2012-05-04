//str2vect.c

#include "../lib/my.h"

char**	my_str2vect(char* string)
{
	unsigned int i = 0; // counter
	char flag;			// flag to test if changing from spaces to a string
	unsigned int s = 0;	// count for number of strings
	unsigned int w; 	// word counter
	unsigned int end;	// begining of word index
	unsigned int bak;	// number of strings
	
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

	//my_str("Number of Words:");
	//my_int(s);
	bak=s;
	
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
				//my_int(s);
				
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
				//my_int(w);
				//my_int(i);
			}
			w++;
		}
	}
	ret[s] = (char*)my_xmalloc(sizeof(char)*(w+1));
	ret[s++] = my_strnconcat(&string[end],"\0", w);
	ret[bak] = NULL;
	return ret;
}
/*	
int main()
{
	char** testing;
	int i;

	testing = str2vect("ls al");
	
	for(i=0; testing[i]!=NULL; i++)
	{
		my_str(testing[i]);
		my_char('|');
	}
}*/
