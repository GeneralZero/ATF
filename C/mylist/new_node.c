//new_node.c

#include "../lib/mylist.h"

t_node*	new_node(void* element, t_node* newnode)
{
	t_node* ret;
	ret = (t_node*)my_xmalloc(sizeof(t_node));
	ret->elem = element;
	ret->next = newnode;
	
	return ret;
}
	
