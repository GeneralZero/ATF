//add_vertex.c

#include "mygraph.h"

boolean add_vertex(t_graph* g, char *n){
     if((g==NULL)||(n == NULL)||((g->v)>=(g->maxv)))
          return FALSE;
     g->vertices[g->v].name = n;
     g->vertices[(g->v)++].visited = FALSE;
     return TRUE;
}
