SRC = addminelement.c addmaxelement.c freeheap.c iicomph.c lookHeap.c newHeap.c popMinHeap.c popMaxHeap.c print_heap.c shiftMaxDown.c shiftMinDown.c shiftMaxUp.c shiftMinUp.c hswap.c
OBJ = $(SRC:.c=.o)
NAME = libmyheap.a
RM = rm -f
TESTS = test.c
TESTO = $(TESTS:.c=.o)
TESTNAME = test
LIBS = -lmyheap
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
