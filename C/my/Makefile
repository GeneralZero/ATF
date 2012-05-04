SRC = my_int.c my_char.c my_revstr.c my_str.c my_digits.c my_alpha.c my_strlen.c my_rfind.c my_find.c my_num_base.c my_vect2str.c my_str2vect.c my_atoi.c\
my_stdstrnconcat.c my_str.c my_strcat.c my_strcpy.c my_strconcat.c my_strcpy.c my_strdup.c my_strindex.c my_strcmp.c my_strnconcat.c my_strncmp.c my_strnconcat.c my_strncpy.c my_strnindex.c my_xmalloc.c my_num_base2.c my_digits2.c
OBJ = $(SRC:.c=.o)
NAME = libmy.a
TMS = main.c
TMO = $(TMS:.c=.o)
TMN = test
LIBS = -lmy
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
