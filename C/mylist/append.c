//append.c

#include "../lib/mylist.h"

void	append(t_node* newnode, t_node** thenode)
{
	if(newnode!=NULL && thenode!=NULL)
	{
		t_node* cnode;
		for(cnode = *thenode; cnode->next!=NULL; cnode = cnode->next);
		cnode->next = newnode;	
	}
}
	
