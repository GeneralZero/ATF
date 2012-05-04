//get_win_size.c

#include "myselect.h"

char	get_win_size()
{
	ioctl(0, TIOCGWINSZ, &gl_env.win);
	//my_int(gl_env.win.ws_col);
	//my_int(gl_env.win.ws_row);
}
