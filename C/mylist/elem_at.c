//elem_at.c

#include "../lib/mylist.h"

void*	elem_at(t_node* thenode, int num)
{
	if(thenode!=NULL && num>0)
		for(num--; thenode!=NULL; thenode = thenode->next, num--)
			if(num==0)
				return thenode->elem;
	return NULL;
}
