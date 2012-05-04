//add_node.c

#include "../lib/mylist.h"

void	add_node(t_node* newnode, t_node** thenode)
{
	if(thenode!=NULL && newnode!=NULL)
	{	
		newnode->next = *thenode;
		*thenode = newnode;
	}
}
