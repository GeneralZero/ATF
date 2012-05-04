//remove_node.c

#include "../lib/mylist.h"

void	remove_node(t_node** thenode)
{
	if(thenode!=NULL && *thenode!=NULL)
	{
		t_node* temp;
		
		temp = *thenode;
		*thenode = (*thenode)->next;
		temp->next = NULL;
		free(temp);
	}
}
