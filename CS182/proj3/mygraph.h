#ifndef _MYGRAPH_H_
#define _MYGRAPH_H_

//#include "../../my.h"
//#include "../proj1/mysorts.h"
#include "../heap/myheap.h"
#include <stdlib.h>
#include <stdio.h>

#ifndef NULL
#define NULL 0
#endif

#ifndef TRUE
#define TRUE 1
#endif

#ifndef FALSE
#define FALSE 0
#endif

#ifndef INF
#define INF 2147483647
#endif 

typedef char boolean;

typedef struct	s_vertex
{
  char		*name;
  boolean	visited;
}		t_vertex;

typedef struct	s_edge
{
  int		src;
  int		dst;
  int		weight;
}		t_edge;

typedef struct	s_graph
{
  t_vertex	*vertices; // list of vertices names and status
  int		**am;  // adjacency matrix
  int		v; // number of vertices
  int		e; // number of edges
  int		maxv; // capacity of vertices (used to allocate am)
  boolean	digraph; // whether it's a digraph or not.
}		t_graph;

t_graph		*new_graph(int);  // REQUIRED creates a new undirected graph with a max of "int" vertices
t_graph		*new_digraph(int); // REQUIRED creates a new digraph
boolean		add_vertex(t_graph *g, char *n); // REQUIRED adds a vertex called n to the graph returns FALSE if there's not more room
boolean		add_edge(t_graph *g, int src, int dst, int w); // REQUIRED adds the edge src->dst with weight w. If the graph is undirected, also adds dst->src
void		show_edges(t_graph *g); // REQUIRED display all edges (HINT: don't display edges going from i to i for example, nor those with infinity
void		show_vertices(t_graph *g); // REQUIRED show the names of all the vertices in the graph
void		dfs(t_graph *g); // REQUIRED perform a dfs traversal of the graph starting at the node at index 0 (show the names of the vertices)
void		dfsrecurse(t_graph *, int); // OPTIONAL used by dfs
void		bfs(t_graph *g); // REQUIRED performs a bfs traversal of the graph starting at the node at index 0 (show the names of the vertices)
void		bfswork(t_graph *g, int); // OPTIONAL used by bfswork
int		*dijkstra(t_graph *g, int); // REQUIRED returns an int array with the shortest distance between the provide node (the int) to every other one. Use INF if the node is unreachable
int		**floyd(t_graph*); // REQUIRED returns an int matrix with the all pairs shortest paths.
int		eecomp(void*, void*); // OPTIONAL used as comparator with the sorting algorithms from libmysorts as well as my priority queue
t_edge		*new_edge(int, int, int); // OPTIONL used all over the place
t_graph		*prim(t_graph *g, int s); // REQUIRED if "kruskal" not implemented otherwise it's optional. Returns a graph holding an MST for the graph g. s is used as the starting point for the prim's algorithm (in case you didn't want it to be 0). 
void		show_am(t_graph*); // OPTIONAL displays the adjacency matrix (if you used one)
t_graph		*getResidualNetwork(t_graph *g); // OPTIONAL used for fordFulkerson
int		augmentPath(t_graph*, int, int, int); // OPTIONAL used for fordFulkerson
t_graph		*fordFulkerson(t_graph*, int, int); // EXTRA CREDIT: Do this for up to 15 extra points


t_graph		*parce(char* file);
t_graph		*parceu(char* file);
int		menu();
int		min(int,int);
boolean		is_digit(char);
int 		find(char*, int, char);
char		*substring(char*, int, int);
#endif
