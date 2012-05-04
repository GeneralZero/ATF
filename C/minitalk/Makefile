TSM = server_main.c
TCM = client_main.c
TCO = $(TCM:.c=.o)
TSO = $(TSM:.c=.o)
TS = server
TC = client
LIBS = -lmy
LIBPATH = ../lib/
RM = rm -f

all: client server
	
client: $(TCO)
	cc -L$(LIBPATH) $(TCO) $(LIBS) -o $(TC)
	
server: $(TSO)
	cc -L$(LIBPATH) $(TSO) $(LIBS) -o $(TS)

debug: $(TSM) $(TCM)
	cc -L$(LIBPATH) -g $(TSO) $(LIBS) -o $(TS)
	cc -L$(LIBPATH) -g $(TCO) $(LIBS) -o $(TC)
	
clean:
	-$(RM) *.o
	-$(RM) *~
	-$(RM) \#*
	-$(RM) *.core

fclean: clean
	-$(RM) $(NAME)
	-$(RM) $(TMN)

re: fclean all
