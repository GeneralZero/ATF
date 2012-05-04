//cleint_main.c

#define _CLIENT_H_

#include "suckittalk.h"

void theEndOfTheCli(int sig)
{
	if(sig == SIGINT)
	{
		my_str("\nEnd of ze Client\n");
		exit(1);
	}
}

int main(int argc, char** argv)
{
	int sockfd;
	int n;
	int port_num;
	
	char buffer[BUFFSIZE];
	char* nname;
	
	struct sockaddr_in server_adderess;

	struct hostent* server;

	if(argc < 3)
	{
		my_str("Use: [Machine_Name] [port_num]\n");
		exit(1);
	}
	
	port_num = my_atoi(argv[2]);
	
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) 
        my_str("ERROR opening socket");
    server = gethostbyname(argv[1]);
	
	if (server == NULL) 
	{
        my_str("ERROR, no such host\n");
        exit(0);
    }
	
	bzero((char*)&server_adderess, sizeof(server_adderess));

	server_adderess.sin_family = AF_INET;
	
	bcopy((char *)server->h_addr, (char *)&server_adderess.sin_addr.s_addr, server->h_length);
	server_adderess.sin_port = htons(port_num);
	
	//my_str("Try connection now\n");
	
	if(connect(sockfd,  (struct sockaddr *)&server_adderess, sizeof(server_adderess))<0)
	{
		my_str("Could not connect to ");
		my_str(argv[1]);
		my_char('\n');
		exit(0);
	}
	signal(SIGINT, theEndOfTheCli);
	//Initilizing Done
	//Starting Program
	
	bzero(buffer, BUFFSIZE);
	nname = (char*)my_xmalloc(50*sizeof(char));
	
	my_str("Nickname: ");
	n = read(0, nname, 49);
	nname[n] = '\0';
	
	
	int i=0;
	while(nname[i] != '\0')
	{
		if(nname[i++] == '\n')
			nname[--i] = '\0';
	}

	if(n <= 0)
		my_str("Invalid nick name\n");
	
	n = write(sockfd, nname, my_strlen(nname));
	
	if(n < 0)
		my_str("ERROR writing to socket\n");
	//my_str(buffer);
	while(1)
	{
		bzero(buffer, BUFFSIZE);
		my_str(nname);
		my_str(": ");
		n = read(0, buffer, BUFFSIZE-1);
		i=0;
		
		while(buffer[i] != '\0')
		{
			if(buffer[i++] == '\n')
				buffer[--i] = '\0';
		}
		
		if(n <= 0)
			my_str("Unable to read\n");
		
		n = write(sockfd, buffer, my_strlen(buffer));
		if(my_strncmp(buffer, "/exit", 5) == 0)
			exit(0);
		if(my_strncmp(buffer, "/nick", 5) == 0)
		{
			free(nname);
			nname = my_strdup(&buffer[6]);
		}
		if(n <= 0)
			my_str("Unable to Write\n");

	}
}