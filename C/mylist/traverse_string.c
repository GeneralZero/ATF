//traverse_string.c

#include "../lib/mylist.h"

void	traverse_string(node* thenode)
{
	if(thenode!=NULL)
		for(; thenode!=NULL; thenode = thenode->next)
		{
			my_str((char*)thenode->elem);
			my_char(' ');
		}
}
