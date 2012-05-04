//input.c

#include "myselect.h"

void	do_select()
{
	if(gl_env.elements[gl_env.pos].mode == 0)
	{
		gl_env.elements[gl_env.pos].mode = 1;
		movedown();
	}
	else
	{
		gl_env.elements[gl_env.pos].mode = 0;
		refresh_out(gl_env.pos);
		refresh_in();
	}
}

char	check_char(char *c)
{
	//my_str(c);
	if (!strcmp(c, SPACE)) 
	{
		//my_str("space ... that means toggle select");
		do_select();
	}
	else if (!strcmp(c, gl_env.up) || !strcmp(c, KU))
	{
		//my_str("up arrow ... that means move up");
		moveup();
	}	
	else if (!strcmp(c, gl_env.down) || !strcmp(c, KD))
	{
		//my_str("down arrow ... that means move down");
		movedown();
	}	
	else if (!strcmp(c, gl_env.left) || !strcmp(c, KL))
	{
		//my_str("left arrow ... that means move left");
		moveleft();
	}	
	else if (!strcmp(c, gl_env.right) || !strcmp(c, KR))
	{
		//my_str("right arrow ... that means move right");
		moveright();
	}	
	else if (!strcmp(c, gl_env.esc) || !strcmp(c, ESC) || !strcmp(c, "\035") || !strcmp(c, "\036") || !strcmp(c, "\037"))
	{
		my_str("escape ... that means exit and DON'T report selected words");
		restore_terminal();
		get_out();
		exit(1);
		return 1;
	}	
	else if (!strcmp(c, ENTER) || !strcmp(c, "\012"))
	{
		//my_str("carriage return ... that means exit and DO report selected words");
		restore_terminal();
		show_selection();
		return 1;
	}
	return 0;
}
