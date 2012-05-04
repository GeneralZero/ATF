//moving.c

#include "myselect.h"

void		moveup()
{
	refresh_out(gl_env.pos);
	if(--gl_env.pos < 0)
		gl_env.pos = gl_env.nbelems - 1;
	refresh_in();
}
	
void		movedown()
{
	refresh_out(gl_env.pos);
	if(++gl_env.pos >= gl_env.nbelems)
		gl_env.pos = 0;
	refresh_in();
}

void		moveleft()
{
	refresh_out(gl_env.pos);
	if((gl_env.pos-= gl_env.win.ws_row) < 0)
		gl_env.pos = 0;
	refresh_in();
}

void		moveright()
{
	refresh_out(gl_env.pos);
	if((gl_env.pos+= gl_env.win.ws_row) > gl_env.nbelems-1)
		gl_env.pos = gl_env.nbelems - 1;
	refresh_in();
}

char*		move_cursor(int x,int y)
{
	char* nums = my_digits2();
	char* x_char = my_num_base2(x, nums);
	char* y_char = my_num_base2(y+1, nums);
	char* ptr ;
	
	ptr = my_strconcat( my_strconcat( my_strconcat( my_strconcat("\033[", y_char), ";"), x_char), "f");
	
	free(nums);
	free(y_char);
	free(x_char);
	return ptr;
}

int		term_move(int x, int y)
{
	char* move = move_cursor(x,y);
	tputs(move, 1, my_termprint);
}

void		term_move_to_item(int i)
{
	term_move(gl_env.elements[i].x, gl_env.elements[i].y);
	//my_int(gl_env.elements[i].x);
	//my_int(gl_env.elements[i].y);
}



