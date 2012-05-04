//server_main.c

#define _SERVER_H_

#include "suckittalk.h"

void term(int sig)
{
	if(sig == SIGINT)
	{
		my_str("\nEnd of ze Server\n");
		exit(0);
	}
}

int main(int argc, char** argv)
{
	int sockfd;
	int sockfd2;
	int port_num;
	int client;
 	int n;
	int l;
	int pid;

	char buffer[BUFFSIZE];
	char* nname ;
	
	struct sockaddr_in server_adderess;
	struct sockaddr_in client_adderess;

	if(argc < 2)
	{
		my_str("Use: [port_num]\n");
		exit(0);
	}
	signal(SIGINT, term);
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	
	if(sockfd < 0)
	{
		my_str("Could not create socket\n");
		exit(0);
	}
	
	bzero((char*)&server_adderess, sizeof(server_adderess));
	//memset();
	
	port_num = my_atoi(argv[1]);
	//my_int(port_num);
	if(port_num < 1 || port_num > 65535)
	{	
		my_str("Invalid Port Number\n");
		exit(0);
	}
	
	server_adderess.sin_family = AF_INET;
	server_adderess.sin_port = htons(port_num);
	server_adderess.sin_addr.s_addr = INADDR_ANY;

	if(bind(sockfd, (struct sockaddr *)&server_adderess, sizeof(server_adderess)) < 0)
	{
		my_str("Could not bind address\n");	
		exit(0);
	}

	listen(sockfd, 5);//can only accept 5 connections at the same exact time
	
	//Server Initilized
	
	//my_str("Server started\n");

	//signal(SIGINT, term);

	while(1)
	{
		//signal(SIGINT, term);
		client = sizeof(client_adderess);
		sockfd2 = accept(sockfd, (struct sockaddr *)&client_adderess, &client);
		if(sockfd2  < 0)
		{
			my_str("Could not Accept Connection\n");
			exit(0);
		}
		else if(sockfd2 == 0)
			my_str("Client Closed\n");
		else
		{

			//signal(SIGINT, term);
			my_str("Client Accepted\n");
		
			if((pid = fork()) < 0)
			{
				my_str("Error forking\n");
				exit(0);
			}
			
			if(pid==0)//Child
			{
				//my_str("Forked");
				//my_int(pid);
				nname =NULL;
				close(sockfd);
				
				n=read(sockfd2, buffer, BUFFSIZE-1);
				buffer[n]='\0';
				nname = my_strdup(buffer);
				my_str("***");
				my_str(nname);
				my_str(" is connected\n");
				
				while(1)
				{
					signal(SIGINT, term);
					bzero(buffer, BUFFSIZE);
					n=read(sockfd2, buffer, BUFFSIZE-1);
					buffer[n]='\0';
					//my_int(n);
					
					//my_str(buffer);
					//my_int(my_strncmp(buffer, "/exit", 4));
					if(my_strncmp(buffer, "/exit", 5) == 0)
					{
						my_str("***");
						my_str(nname);
						my_str(" has disconnected\n");
						close(sockfd2);
						free(nname);	
						exit(0);
					}
					else if(my_strncmp(buffer, "/me", 3) == 0)
					{
						my_str(nname);
						my_char(' ');
						my_str(&buffer[4]);
						my_char('\n');
					}

					else if(my_strncmp(buffer, "/nick", 5) == 0)
					{
						my_str("***");
						my_str(nname);
						my_str(" was changed to ");
						my_str(&buffer[6]);
						my_char('\n');
						nname = my_strdup(&buffer[6]);
					}

					else
					{
						my_str(nname);
						my_str(": ");
						my_str(buffer);
						my_char('\n');
					}
				}
			}
			close(sockfd2);
		}
	}
}
