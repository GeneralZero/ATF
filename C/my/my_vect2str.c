//my_vect2str.c

#include "../lib/my.h"

char*	my_vect2str(char** args)
{
	int count;
	int i;
	char* ret;
	
	for(i = 0, count = 0; args[i] !=NULL; i++, count+= my_strlen(args[i]));
	
	ret = my_xmalloc(sizeof(char)* count);
	for(i =0; args[i]!='\0'; i++)
	{
		ret = my_strcat(ret, args[i]);
		ret = my_strcat(ret, " ");
	}
	
	ret = my_strcat(ret,"\0");
	
	return ret;
}
