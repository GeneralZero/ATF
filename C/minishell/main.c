//main.c

#include <unistd.h>

#include "../lib/my.h"

#define BUFFSIZE 1024

int main(int argc, char** argv)
{
	unsigned int n;
	unsigned int pid;
	
	char** exe;
	
	char* buff = (char*)my_xmalloc(sizeof(char)*BUFFSIZE); 
	char* dir = (char*)my_xmalloc(sizeof(char)*BUFFSIZE); 
	int i=0;	
	
	while(1)
	{
		my_str("Awesome@Yes:");
		n=read(0, buff, BUFFSIZE-1);
		buff[n-1] = '\0';
		//my_str(buff);
		exe = my_str2vect(buff);
		
		/*for(i=0; exe[i]!=NULL; i++ )
			my_str(exe[i]);*/
		
		
		//my_int(n);
		//my_str(buff);
		//my_int(my_strncmp("cd", buff, 2));
		//my_int(my_strncmp("exit", buff, 4));
		if(n>1)
		{

			if(my_strncmp("exit", buff, 4) == 0)
				//my_str("Closing\n");
				exit(0);
		
			else if(my_strncmp("cd", buff, 2) == 0)
			{
				dir = "\0";
				//my_int(chdir(exe[1]));
				//my_int(exe[1][0] == '/');
				if(exe[1][0] == '/')
				{
					if( chdir(exe[1])<0)
						my_str("Directory doesn't Exist\n");
				}
				else
				{
					if(chdir(my_strconcat(my_strconcat(getcwd(dir, BUFFSIZE-1), "/") ,exe[1]))<0)
						my_str("Directory doesn't Exist\n");
				}
				//my_str(my_strconcat(my_strconcat(getcwd(buff, BUFFSIZE-1), "/") ,exe[1]));
				//my_str(exe[1]);
			}
			else
			{
				if((pid = fork())<0)
					my_str("Error with Forking 1.\n");
			
				else if(pid == 0)
				{
					//my_str("execpv: \n");
					//my_str(exe[1]);//execpv
					//my_int(execvp(exe[0], exe));
					
					if(execvp(*exe, exe)<0)
						my_str("invalid command\n");
					exit(0);
				
				}
				else
				{
					wait();
					//my_str("Finished Executing\n");
				}
			}	
		}
	}
	free(buff);
	free(dir);
	for(i=0; exe[i]!=NULL; i++)
		free(exe[i]);
}

#undef BUFFSIZE
