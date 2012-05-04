//show_elems.c

#include "myselect.h"

void	show_elems()
{	
	int i;
	int x;
	int y;
	int max;
	char space = 5;
	
	get_win_size();
	gl_env.flag = 0;
	term_clear();
	//my_int(gl_env.nbelems);
	for(i=0, x=0, y=0, max=0; i<gl_env.nbelems; i++, y++)
	{
		//my_int(gl_env.win.ws_row);
		if(y>= gl_env.win.ws_row)
		{
			x+=(max+ space);
			y=0;
			max=0;
		}
		
		if(max <gl_env.elements[i].size)
			max = gl_env.elements[i].size;
		if((x+max) >= gl_env.win.ws_col)
		{
			term_clear();
			gl_env.flag = 1;
			term_move(0,0);
			my_str("Please Enlarge Window");
			break;
		}
		
		gl_env.elements[i].x = x;		
		gl_env.elements[i].y = y;
		//my_int(max);
		refresh_out(i);
		//my_int(max);
	}
	
	if(!gl_env.flag)
		refresh_in();
}
