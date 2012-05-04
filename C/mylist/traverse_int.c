//traverse_int.c

#include "../lib/mylist.h"

void	traverse_int(node* thenode)
{
	if(thenode!=NULL)	
		for(; thenode!=NULL; thenode = thenode->next)
			my_int(*((int*)(thenode->elem)));
		
}
