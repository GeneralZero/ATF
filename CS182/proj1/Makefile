SRC = cccomp.c iicomp.c sscomp.c ppcomp.c insertSort.c mergeSort.c recMergeSort.c radixSort.c swap.c
OBJ = $(SRC:.c=.o)
NAME = libmysorts.a
TMS = main.c
TMO = $(TMS:.c=.o)
TMN = test
LIBS = -lmysorts
LIBPATH = .
RM = rm -f

all: $(OBJ)
	ar -rc $(NAME) $(OBJ)
	ranlib $(NAME)

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
