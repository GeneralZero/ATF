//remove_node_at.c

#include "../lib/mylist.h"

void	remove_node_at(t_node** thenode, int num)
{
	if(thenode!=NULL && *thenode!=NULL)	
	{
		if(num<1)
			remove_node(thenode);
		else if(num>count_nodes(*thenode))
			remove_last(thenode);
		else
		{
			t_node* temp;
			t_node* head;
			for(temp = *thenode; 0<num;temp = temp->next, num--);	
				head = temp->next;
				temp->next = (temp->next)->next;
				head->next = NULL;
				free(head);
		}
	}
} 
