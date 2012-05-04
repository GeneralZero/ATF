//remove_last.c

#include "../lib/mylist.h"

void	remove_last(t_node** thenode)
{
	if(thenode!=NULL && *thenode!=NULL)
	{	
		t_node* cnode;
		t_node * head;
		for(head = *thenode, cnode = *thenode; (cnode->next)!=NULL;head = cnode, cnode = cnode->next);
			
		free(head->next);
		head->next = NULL;
	}
}
