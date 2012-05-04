//add_elem.c

#include "../lib/mylist.h"

void	add_elem(void* element, t_node** thenode)
{
	if(thenode!=NULL && element != NULL)
	{	
		t_node* n = new_node(element, *thenode);
		*thenode = n;
	}
}
