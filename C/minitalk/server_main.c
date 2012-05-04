//server_main.c

#include "minitalk.h"

t_env	gl_env;

void recursive_int(int sig)
{
	static short count = 0;
	static pid_t c = 0;
	
	//my_int(c);
	
	c = c << 1;
	if(sig == SIGUSR2)
		c |= 1;
	if(++count == sizeof(pid_t)*8)
	{
		//my_int(c);
		gl_env.cpid = c;
		//gl_env.sigflag = 1;
		c=0;
		count=0;
	}
	
}

void recursive_char(int sig)
{
	static char count = 0;
	static char c = 0;

	c = c << 1;
	if(sig == SIGUSR2)
		c |= 1;
	if(++count == sizeof(char)*8)
	{
		count = 0; 
		if(c != '\0')
			my_char(c);
		else
		{
		//my_str("reachedflag");
	            gl_env.sigflag = 1;
		}
		c = 0;
	}
	
	kill(gl_env.cpid, SIGUSR2);
}

void serv_exit(int sig)
{
	if(sig == SIGINT)
	{
		my_str("\nSomebody set up us the bomb.\n");
		exit(0);
	}
}


int main(int argc, char** argv)
{
	int pid = getpid();
	int i;
	
	signal(SIGINT, serv_exit);
	
	my_str("Server PID: ");
	my_int(pid);
	my_str("\n");
	
	while(1)
	{
		gl_env.cpid = 0;
		gl_env.sigflag = 0;
		//my_str("before loop");
		
		signal(SIGUSR1, recursive_int);
		signal(SIGUSR2, recursive_int);
		
		//my_str("PID loop");
		
		for(i = 0; i < sizeof(pid_t)*8; i++)
		{
			//my_str("in for loop");
			pause();
		}
		//my_str("after for loop");
		my_str("Client PID: ");
		my_int(gl_env.cpid);
		//my_str("\n");

		kill(gl_env.cpid, SIGUSR1);

		signal(SIGUSR1, recursive_char);
		signal(SIGUSR2, recursive_char);
		
		my_str("Receved: ");
		while(!gl_env.sigflag)
		{
			pause();
		}
		my_char('\n');
	}
}
