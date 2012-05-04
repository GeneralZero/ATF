//main.c

#include "myselect.h"

int main(int argc, char** argv)
{
	int n;
	char buffer[4];
	
	if(argc <= 1)
	{
		my_str("Use: ./myselect opt1 [opt2 ....]");
		exit(0);
	}	
	
	init_terminal();			//
	init_caps();				//backup shell caps

	//my_str("past set up\n");
	setup_elem(argc, argv);	//set up element array
	signal(SIGWINCH, show_elems);
	term_vi();
	
	term_clear();
	show_elems();
	//my_int(gl_env.nbelems);
	while(1)
	{	
		n = read(0, buffer, READMIN);	
		buffer[n] = '\0';
		//check_char(buffer);
		if(check_char(buffer))
			break;
	}

	get_out(1);		//restore inital caps
	return 0;
}
