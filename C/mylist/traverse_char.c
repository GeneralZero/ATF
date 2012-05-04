//traverse_char.c

#include "../lib/mylist.h"

void	traverse_char(node* thenode)
{
	if(thenode!=NULL)
		for(; thenode!=NULL; thenode = thenode->next)
		{
			my_char(*((char *)(thenode->elem)));
			my_char(' ');
		}
}
