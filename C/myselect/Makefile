SRC = main.c initialWork.c endWork.c printing.c input.c refresh.c show_elems.c moving.c get_win_size.c
OBJ = $(SRC:.c=.o)
NAME = my_select
LPATH = ../lib
LIBS = -lmy -ltermcap
RM = rm -f

all: $(OBJ)
	cc -L$(LPATH) $(OBJ) $(LIBS) -o $(NAME)

clean:
	-$(RM) *.o
	-$(RM) \#*
	-$(RM) *~
	-$(RM) *.core

fclean: clean
	-$(RM) $(NAME)
