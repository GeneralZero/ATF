//my_xmalloc.c

#include "../lib/my.h"

void*	my_xmalloc(int size)
{
	void* ret;
	ret=malloc(size);
	
	if(ret==NULL)
	{
		my_str("Virtual Memory exausted\n");
		exit(1);
	}
	return ret;
}
	
