SRC = new_ihashtable.c ihashadd.c ihashremove.c freeihash.c ihashcleanup.c ihashsearch.c
OBJ = $(SRC:.c=.o)
NAME = libMyiHash.a
RM = rm -f
TESTS = main.c
TESTO = $(TESTS:.c=.o)
TESTNAME = test
LIBS = -lMyiHash
LPATH = .

all: $(OBJ)
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
