//parce.c

#include "mygraph.h"
	
t_graph* parce(char* files){
	const int MAX = 100;
	char c = '|';
	FILE* fp;
	fp = fopen(files, "r");
	t_graph* theGraph;
	char sub[10];
	char file[100]; 
	while((fgets(file,MAX,fp))!= NULL){
		int i,j,k,start=0,end;
		if(is_digit(file[0])){
			end=find(file, MAX, c);
			i=atoi(substring(file,0,end));
			//printf("%d", i);
			theGraph = new_digraph(i);
		}
		if(file[0] == 'E'){
			start = find(file, MAX, c)+1;
			end = find(&file[start], MAX, c)+start;
			i=atoi(substring(file,start,end));
			//printf("%d\n", i);
					
			start= end+1;
			end = find(&file[start], MAX, c)+start;	
			j=atoi(substring(file,start,end));
			//printf("%d\n", j);

			start= end+1;
			end = 2+start;
			k=atoi(substring(file,start,end));
			printf("%d %d\n", start,end);
			add_edge(theGraph, i, j, k);

		}
		if(file[0] == 'V'){
			start = find(file, MAX, c)+1;
			end = find(&file[start], MAX, c)+start;
			//printf("%s\n", substring(file,start,end));
			add_vertex(theGraph, substring(file,start,end));

			start= end+1;
			end = start+2;
			//printf("%d\n", atoi(substring(file,start,end)));
		}
	}
	return theGraph;
}

boolean is_digit(char c) {
	if( c >= '0' && c <= '9' )
		return TRUE;
	return FALSE;
}

int find(char* array, int size, char index){
	int i;
	for(i=0;i<size;i++)
		if(array[i] == index)
			return i;
	return FALSE;
}

char* substring(char* array, int start, int end){
	int i,count;
	char* ret = (char*)malloc(sizeof(char)*(end-start+1));
	if(start<end){
		for(count=0,i=start; count<end-start; count++,i++){
			ret[count] = array[i];
		}
	}
	return ret;
}
