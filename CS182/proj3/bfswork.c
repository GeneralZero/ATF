//bfswork.c

#include "mygraph.h"

void bfswork(t_graph *g, int k){
	if((k>=0)&&(g!=NULL)&&(k<=g->maxv)){
		int i,j=0,start=0;
		int* arr = (int*)malloc(sizeof(int)*g->maxv);
		for(i=0;i<g->maxv;i++){
			if(g->am[k][i]!=0 && g->vertices[i].visited==FALSE){
				printf("%s\n", g->vertices[i].name);
				g->vertices[i].visited=TRUE;
				arr[j++] = i;
			}
		}
		for(i=0; i<j;i++)
			bfswork(g,arr[start++]);
	}
}
