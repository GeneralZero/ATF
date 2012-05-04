//add_edge.c

#include "mygraph.h"

boolean add_edge(t_graph* g, int src, int dst, int w){
	if((g==NULL)||(src<0)||(dst<0)||(w<0)||(src>=g->maxv)||(dst>=g->maxv))
		return FALSE;
	g->am[src][dst] = w;
	if(!(g->digraph))
		g->am[dst][src] = w;
	g->e++;
	return TRUE;
}
