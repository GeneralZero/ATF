SRC = add_elem.c add_node.c add_node_at.c append.c count_nodes.c elem_at.c empty_list.c new_node.c remove_last.c remove_node.c remove_node_at.c traverse_int.c traverse_char.c traverse_string.c
OBJ = $(SRC:.c=.o)
NAME = libmylist.a
TMS = mainlistsample.c
TMO = $(TMS:.c=.o)
TMN = test
LIBS = -lmylist -lmy
LIBPATH = ../lib/
RM = rm -f

all: $(OBJ)
	ar -rc $(NAME) $(OBJ)
	ranlib $(NAME)
	mv $(NAME) $(LIBPATH)

test: all $(TMO)
	cc -L$(LIBPATH) $(TMO) $(LIBS) -o $(TMN)

clean:
	-$(RM) *.o
	-$(RM) *~
	-$(RM) \#*
	-$(RM) *.core

fclean: clean
	-$(RM) $(NAME)
	-$(RM) $(TMN)

re: fclean all
