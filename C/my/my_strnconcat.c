//my_strnconcat.c

#include "../lib/my.h"

char*	my_strnconcat(char* string1, char* string2, int num)
{
	char* ret = NULL;
	if(string1==NULL && string2== NULL)
		return ret;
	/*else if(string1==NULL)
		return string2;
	else if(string2==NULL)
		return string1;*/
	else
	{
		int count = 0;
		int length = my_strlen(string2)+my_strlen(string1)-1;
		if (length>=num)
			length = num;
		if(length<1)
			length = 1;
		ret=(char*)my_xmalloc(length*sizeof(char));
		if(string1!=NULL)
			for(; *string1!='\0' && count<num;(string1)++)
				ret[count++] = *string1;
		//my_int(count);
		if(string2!=NULL)
			for(;*string2!='\0' && count<num; string2++)
				ret[count++] = *string2;
		ret[++count] = '\0';
	}
	return ret;
}
