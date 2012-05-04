//empty_list.c

#include "../lib/mylist.h"

void	empty_list(t_node** thenode)
{
	for(; *thenode!=NULL;)
		remove_node(thenode);
}
