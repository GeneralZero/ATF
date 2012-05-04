SRC = add_edge.c add_vertex.c bfs.c bfswork.c dijkstra.c dfs.c dfsrecurse.c eecomp.c floyd.c menu.c new_digraph.c new_edge.c new_graph.c parce.c parceu.c show_am.c show_edges.c show_vertices.c prim.c
OBJ = $(SRC:.c=.o)
NAME = libMyGraph.a
RM = rm -f
TESTS = main.c
TESTO = $(TESTS:.c=.o)
TESTNAME = test
LIBS = -lMyGraph -lmyheap
LPATH = .

all:$(OBJ)
	ar -rc $(NAME) $(OBJ)
	ranlib $(NAME)

clean:
	-$(RM) *.o
	-$(RM) *~
	-$(RM) \#*
	-$(RM) *.core

fclean: clean
	-$(RM) $(NAME)

re: fclean all

test: $(TESTO) $(NAME)
	cc -L$(LPATH) $(TESTO) $(LIBS) -o $(TESTNAME)

$(NAME): all
