//input.c

#include "myselect.h"

void	do_select()
{
	gl_env.elements[gl_env.pos].mode = 1;
	movedown();
}

char	check_char(char *c)
{
	int i;
	if (!strcmp(c, SPACE)) 
	{
		my_str("space ... that means toggle select");
		//do_select();
	}
	else if (!strcmp(c, gl_env.up))
	{
		my_str("up arrow ... that means move up");
		//moveup();
	}	
	else if (!strcmp(c, gl_env.down))
	{
		my_str("down arrow ... that means move down");
		//movedown();
	}	
	else if (!strcmp(c, gl_env.left))
	{
		my_str("left arrow ... that means move left");
		//moveleft();
	}	
	else if (!strcmp(c, gl_env.right))
	{
		my_str("right arrow ... that means move right");
		//moveright();
	}	
	else if (!strcmp(c, gl_env.esc))
	{
		my_str("escape ... that means exit and DON'T report selected words");
		restore_terminal();
	}	
	else if (!strcmp(c, gl_env.clear))
	{
		my_str("carriage return ... that means exit and DO report selected words");
		restore_terminal();
	}
	else 
		return 0;
	return 1;
}
