//refresh.c

#include "myselect.h"

void		refresh_in()
{
	term_move_to_item(gl_env.pos);
	term_underline();
	if(gl_env.elements[gl_env.pos].mode == 1)
		term_standout();
	if(gl_env.elements[gl_env.pos].elem != NULL)
		my_str(gl_env.elements[gl_env.pos].elem);
	//my_char('<');
	term_underend();
	term_standend();
}
	
void		refresh_out(int i)
{
	term_move_to_item(i);
	term_underend();
	if(gl_env.elements[i].mode == 1)
		term_standout();
	if(gl_env.elements[i].elem != NULL)
		my_str(gl_env.elements[i].elem);
	//my_char('<');
	//my_int(i);
	term_standend();
}
