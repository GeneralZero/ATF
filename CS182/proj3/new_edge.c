//*new_edge.c

#include "mygraph.h"

t_edge* new_edge(int src, int dst, int w){
	if(src<0 ||dst<0 || w<=0)	
		return NULL;
	t_edge* temp = (t_edge*)malloc(sizeof(t_edge));
	temp->src = src;
	temp->dst = dst;
	temp->weight = w;
	return temp;
}
