//client_main.c

#include "minitalk.h"

t_env	gl_env;

void send_pid(pid_t mypid)
{
	int i;
	pid_t mask = 1<<(8*sizeof(pid_t)-1);
	
	for(i=0; i<sizeof(pid_t)*8; i++)
	{
		if(mask&mypid)
			kill(gl_env.cpid, SIGUSR2);	//my_char('1');
		else
			kill(gl_env.cpid, SIGUSR1);	//my_char('0');
		mypid = mypid << 1;
		usleep(2000);
	}
}

void sig_USR2(int sig)
{
	gl_env.sigflag = gl_env.sigflag;
}

void send_char(char output)
{
	int i,j;	
	char mask = 1 << (8*sizeof(char)-1);
	
	for(j=0; j<8*sizeof(char); j++)
	{
		if(mask&output)
		{
			kill(gl_env.cpid, SIGUSR2);
			//my_char('1');
		}
		else
		{
			kill(gl_env.cpid, SIGUSR1);
			//my_char('0');
		}
		output = output << 1;
		signal(SIGUSR2,sig_USR2);
		pause();
		//signal(SIGUSR2,sig_USR2);
	}
}

void sig_ALRM(int sig)
{
	exit(0);
}

void sig_USR1(int sig)
{
	gl_env.sigflag = 1;
}

int main(int argc, char** argv)
{
	if(argc>2)
	{
		char*	message = my_vect2str(&argv[2]);
		int size = my_strlen(message);
		int i;
		
		//my_str(message);
		gl_env.sigflag =0;
		gl_env.cpid = my_atoi(argv[1]);
		
		signal(SIGUSR1,sig_USR1);
		signal(SIGALRM,sig_ALRM);
		
		send_pid(getpid());
		//my_int(getpid());
		
		if(!gl_env.sigflag)
		{
			alarm(2);
			pause();
		}
		alarm(0);
		
		my_str("Sending:");
		
		for(i=0; i<size; i++)
		{
			my_char(message[i]);
			send_char(message[i]);
		}
		send_char('\0');
		my_char('\n');
		
	}
	else
		my_str("Use: server_PID [arg2 ...]\n");
}
