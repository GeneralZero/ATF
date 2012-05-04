//prim.c

#include "mygraph.h"

t_graph* prim(t_graph *g, int s){
	if(g==NULL||s<0 || s>g->maxv)
		return NULL;
	int i;
	t_graph* ret = new_graph(g->maxv);
	t_edge* temp = (t_edge*)malloc(sizeof(t_edge));
	t_heap* theHeap = newHeap(g->maxv);
	for(i=0;i<g->maxv;i++)
		g->vertices[i].visited = FALSE;
	g->vertices[s].visited = TRUE;
	printf("%s\n",g->vertices[s].name);
	for(i=0;i<g->maxv;i++){
		if(g->am[s][i]!=0){
			add_edge(ret,s,i,g->am[s][i]);
			addMinElement(theHeap,(void*)new_edge(s,i,g->am[s][i]),&eecomp);
		}
	}
	while(theHeap->current_size>0){
		temp = (t_edge*)popMinHeap(theHeap,&eecomp);
		g->vertices[temp->dst].visited = TRUE;
		printf("%s\n",g->vertices[temp->dst].name);
		for(i=0;i<(g->maxv);i++){
			if(g->am[temp->dst][i]!=0&&g->vertices[i].visited ==FALSE){
				addMinElement(theHeap,(void*)new_edge(temp->dst,i,g->am[temp->dst][i]),&eecomp);
				add_edge(ret,temp->dst,i,g->am[temp->dst][i]);
			}
		}
	}
	return ret;	
}
