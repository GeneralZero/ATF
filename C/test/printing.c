//printing.c

#include "myselect.h"

void term_standend()
{
	tputs(gl_env.stand_end, 1, my_termprint);
}

void term_standout()
{
	tputs(gl_env.standout, 1, my_termprint);
}

void term_clear()
{
	tputs("\033[2J", 1, my_termprint);
	//my_char('p');
}

void		term_underline()
{
	tputs(gl_env.underline, 1, my_termprint);
}

void		term_underend()
{
	tputs(gl_env.under_end, 1, my_termprint);
}

void		term_ve()
{
	tputs(gl_env.cursoron, 1, my_termprint);
}

void		term_vi()
{
	tputs(gl_env.cursoroff, 1, my_termprint);
}

int		my_termprint(int c)
{
	return write(1, &c, 1);
}
