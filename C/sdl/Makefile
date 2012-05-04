SRC = image.c
OBJ = $(SRC:.c=.o)
OUT = test
RM = rm -f
LIB = SDL

all: 
	gcc -c $(SRC) 
	gcc -l$(LIB) $(OBJ) -o $(OUT)
	./$(OUT)

test: all
	./$(OUT)
	
clean:
	$(RM) *.o
	$(RM) *~
	$(RM) \#*
	$(RM) *.core


fclean: clean
	-$(RM) $(OUT)

re: fclean all
