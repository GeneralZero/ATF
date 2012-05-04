//my_strconcat.c

#include "../lib/my.h"

char*	my_strconcat(char* string1, char* string2)
{
	char* ret = NULL;
	if(string1==NULL && string2== NULL)
		return ret;
	else if(string1==NULL)
		return string2;
	else if(string2==NULL)
		return string1;
	else
	{
		int count;
		int length = my_strlen(string2)+my_strlen(string1)-1;
		ret=(char*)my_xmalloc(length*sizeof(char));
		
		for(count=0; *string1!='\0';(string1)++)
			ret[count++] = *string1;
			
		for(;*string2!='\0'; string2++)
			ret[count++] = *string2;
		ret[++count] = '\0';
	}
	return ret;
}
