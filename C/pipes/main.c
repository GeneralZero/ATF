//main.c

#include "../lib/my.h"

int main(int argc, char** argv)
{
	int gp_pid;  //grandparent process
	int p_pid; //parent process
	
	int pipes1[2];//pipe between Grandparent and Parent
	int pipes2[2];//pipe between Parent and Child
	
	int n;
	int buffsize = 32;
	char* buff = my_xmalloc(sizeof(char)*buffsize);
	
	char* message;// = "Hello";
	char* buff2 = my_xmalloc(sizeof(char)*buffsize); //buffer2
	
	if(argc < 2)
	{
		my_str("Use: arg1 [arg2 ...]");
	}
	else
	{
		message = my_vect2str(&argv[1]);
		pipe(pipes1);
	
		if((gp_pid = fork())<0)
		{
			my_str("Error with Forking 1.");
			my_char('\n');
			exit(1);
		}
		
		else if(gp_pid == 0)// Parrent Process
		{		
			pipe(pipes2);
		
			close(pipes1[0]);
		
			if((p_pid = fork())<0)
			{
				my_str("Error with Forking 2.");
				my_char('\n');
				exit(1);
			}
		
			else if(p_pid == 0)// Child Process
			{
				close(pipes2[0]);
				my_str("The Child is passing a string to the parrent");
				my_char('\n');
				write(pipes2[1], message, my_strlen(message));
			
				//close(pipes2[1]);
			}
		
			else //parrent Process
			{
				close(pipes2[1]);
				wait();
				my_str("The Parrent is reading from the child");
				my_char('\n');
				n=read(pipes2[0], buff2, buffsize-1);
				buff[n] = '\0';
				my_str("Printing the passed string:");
				my_char('\n');
				my_str(buff2);
				my_char('\n');
				my_str("The Parrent is passing a string to the Grandparrent");
				my_char('\n');
				write(pipes1[1], buff2, n);
			
				//close(pipes1[1]);
			}
		
			//close(pipes1[0]);
			//free(buff2);
			exit(1);
		}
		else// Grandparent Process
		{
			close(pipes1[1]);
			wait();
			my_str("The Grandparrent is reading from the parrent");
			my_char('\n');
			n=read(pipes1[0], buff, buffsize-1);
			buff[n] = '\0';
			my_str("Printing the passed string:");
			my_char('\n');
			my_str(buff);
			my_char('\n');
		}
		//free(buff);
	}
	free(buff);
	free(buff2);
	exit(1);
}
