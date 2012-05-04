//initialWork.c

#include "myselect.h"

void 	init_terminal()
{
	char* name;
	int fd;
	struct termios ts;

	name  = ttyname(0);
	fd = open(name, O_WRONLY);
	
	gl_env.stdio_backup = dup(1);
	dup2(fd, 1);
	
	//my_str("setting up terminal\n");
	  
	if(tcgetattr(fd, &(gl_env.line_backup)) < 0)
	{
		my_str("Error: linebakup");
		exit(1);
	}	
	ts = gl_env.line_backup;	
	ts.c_lflag &= ~(ICANON | ECHO | ISIG);
	ts.c_cc[VTIME] = 1;
	ts.c_cc[VMIN] = 3;

	if(tcsetattr(fd, TCSAFLUSH, &ts) < 0)
	{
		my_str("Error with tcsetattr");
		exit(1);
	
	}

	get_win_size();

	//setbuff(1, NULL);
	//my_int(gl_env.win.ws_col);
	//my_int(gl_env.win.ws_row);
	
	//my_str("Finished terminal set up\n");
	
}

void setup_elem(int argc, char** argv)
{
	glob_t gt;
	int i;
	//my_str("before glob");
	glob(argv[1], GLOB_NOCHECK | GLOB_ERR, NULL, &gt);//
		
	for (i = 2; i < argc; i++)
	{
		glob(argv[i], GLOB_NOCHECK | GLOB_ERR | GLOB_APPEND, NULL, &gt);
	}
	
	gl_env.elements =(t_elem*)my_xmalloc(gt.gl_pathc*sizeof(t_elem));
	
	//my_int(gl_env.win.ws_row);
	//my_int(gt.gl_pathc);
	for(i=0; i<gt.gl_pathc; i++)
	{
		//my_str(gt.gl_pathv[i]);
		//my_str("0");
		gl_env.elements[i].elem = my_strdup(gt.gl_pathv[i]);
		//my_str("1");
		gl_env.elements[i].size = my_strlen(gt.gl_pathv[i]);
		//my_str("2");
		gl_env.elements[i].x = 0;
		//my_str("3");
		gl_env.elements[i].y = i%(gl_env.win.ws_row);
		//my_str("4");
		gl_env.elements[i].mode = 0;
		//my_str("5");
	}
	//my_int(gt.gl_pathc);
	gl_env.nbelems=gt.gl_pathc;
	//my_str("after blob setup");
	gl_env.pos = 0;
	//my_char('l');
	//my_str(gl_env.elements[4].elem);
	//my_int(gl_env.elements[1].y);
}

void	init_caps()
{	
	char area[2048];
	char* ptr;
	char tempBuff[1024];

	//my_str("1");
	
	if((ptr = (char *)getenv("TERM")) == NULL)
	{
		my_str("Error: getenv term");
		exit(1);
	}
	
	if((tgetent( tempBuff, ptr )) < 0)
	{
		my_str("Error: tgetent term");
		exit(1);
	}
	
	//my_str("Starting caps set up\n");
	
	if(!(gl_env.up = tgetstr(UP, (char**)(&area))))
	{
		gl_env.up = KU;
		my_str("up");
	}
	if(!(gl_env.down = (char *)tgetstr(DOWN, (char**)(&area))))
	{
		gl_env.down = KD;
		my_str("down");
	}	
	if(!(gl_env.left = (char *)tgetstr(LEFT, (char**)(&area))))
	{
		gl_env.left = KL;
		my_str("left");
	}	
	if(!(gl_env.right = (char *)tgetstr(RIGHT, (char**)(&area))))
	{
		gl_env.right = KR;
		my_str("right");
	}
	if(!(gl_env.clear = (char *)tgetstr(CLEAR, (char**)(&area))))
	{
		my_str("Error with seting clear");
		exit(1);
	}
		
	if(!(gl_env.move = (char *)tgetstr(MOVE, (char**)(&area))))
	{
		my_str("Error with seting clear");
		exit(1);
	}
		
	if(!(gl_env.standout = (char *)tgetstr(STANDOUT , (char**)(&area))))
	{
		my_str("Error with seting start highlite");
		exit(1);
	}
		
	if(!(gl_env.stand_end = (char *)tgetstr(STAND_END, (char**)(&area))))
	{
		my_str("Error with seting stop highlight");
		exit(1);
	}
		
		
	if(!(gl_env.underline = (char *)tgetstr(UNDERLINE, (char**)(&area))))
	{
		my_str("Error with seting start underline");
		exit(1);
	}
		
	if(!(gl_env.under_end = (char *)tgetstr(UNDER_END, (char**)(&area))))
	{
		my_str("Error with seting end underline");
		exit(1);
	}
		
	if(!(gl_env.cursoroff = (char *)tgetstr(CURSOROFF, (char**)(&area))))
	{
		my_str("Error with seting cursor off");
		gl_env.cursoroff = VECAP;
	}
	
	if(!(gl_env.cursoron = (char *)tgetstr(CURSORON, (char**)(&area))))
	{
		gl_env.cursoron = VICAP;
		my_str("Error with seting cursor on");
        }

	char* exc = (char*)my_xmalloc(2*sizeof(char));
	exc[0] = *((char*)ESC);
	exc[1] = '\0';
	gl_env.esc = exc;

        //my_str("Finished caps set up\n");
}
