//add_node_at.c

#include "../lib/mylist.h"

void	add_node_at(t_node* element, t_node** thenode, int num)
{
	if(thenode!=NULL && element!=NULL)
	{
		t_node* point;

		if(num<1)
			add_node(element, thenode);
		else if(num > count_nodes(*thenode))
			append(element, thenode);
		else
		{
			for(num--,point = *thenode; 0 < num; point = point->next, num--);
			element->next = point->next;
			
			point->next = element;
		}
	}
}	
