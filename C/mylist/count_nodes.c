//count_nodes.c

#include "../lib/mylist.h"

int		count_nodes(t_node* thenode)
{
	int i = 0;
	if(thenode != NULL)
	{
		for(; thenode->next!=NULL; thenode = thenode->next, i++);
		i++;
	}
	return i;
}
