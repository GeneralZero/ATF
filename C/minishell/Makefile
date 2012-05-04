TMS = main.c
TMO = $(TMS:.c=.o)
TMN = test
LIBS = -lmy
LIBPATH = ../lib
RM = rm -f

all: $(TMO)
	cc -L$(LIBPATH) $(TMO) $(LIBS) -o $(TMN)

debug:
	cc -c -g $(TMS) -o $(TMO)
	cc -L$(LIBPATH) -g $(TMO) $(LIBS) -o $(TMN)
	
clean:
	-$(RM) *.o
	-$(RM) *~
	-$(RM) \#*
	-$(RM) *.core

fclean: clean
	-$(RM) $(NAME)
	-$(RM) $(TMN)

re: fclean all
