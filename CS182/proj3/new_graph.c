//new_graph.c

#include "mygraph.h"

t_graph* new_graph(int k){
	if(k<=0)
		return NULL;
	t_graph* ret;
	if (k>=1){
		int i,j;
		ret = (t_graph*)malloc(sizeof(t_graph));
		ret->vertices = (t_vertex*)malloc(sizeof(t_vertex)*k);
		ret->maxv = k;
		ret->e = 0;
		ret->v = 0;
		ret->digraph = FALSE;
		ret->am = (int**)malloc(sizeof(int*)*k);
		for(i=0;i<k;i++)
			ret->am[i] = (int*)calloc(k,sizeof(int));
     }
	return ret;
}
