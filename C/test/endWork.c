//endWork.c

#include "myselect.h"

void show_selection()
{
	int i;
	for(i=0; i<gl_env.nbelems-1; i++)
		if(gl_env.elements[i].mode)
		{
			my_str(gl_env.elements[i].elem);
			my_char(' ');
		}
	/*if(gl_env.elements[gl_env.nbelems-1].mode)
	{
		gl_env.elements[gl_env.nbelems-1].elem[gl_env.elements[gl_env.nbelems-1].size] = '\0';
		my_str(gl_env.elements[gl_env.nbelems-1].elem);
	}*/
}

int no_files()
{
		my_str("No files matched input");
		restore_terminal();
		exit(1);
}

void	restore_terminal()
{
	term_ve();
	
	tcsetattr(1, TCSAFLUSH, &gl_env.line_backup);
	dup2(gl_env.stdio_backup, 1);
}

void get_out()
{
	int i;
	for(i=0; i<gl_env.nbelems-1; i++)
	{
		free(gl_env.elements[i].elem);
	}
	
	//free(gl_env.elements);
	//free(gl_env.esc);
}
