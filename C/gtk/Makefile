TMS = night_day.c
TES = exit_clicked.c image_button.c destroy.c day_clicked.c close_clicked.c night_clicked.c no_clicked.c
TMO = $(TMS:.c=.o)
TEO = $(TES:.c=.o)
TC = gui
RM = rm -f
CFLAGS = `pkg-config --cflags gtk+-2.0`
LIBS   = `pkg-config --libs gtk+-2.0`

	
all: 
	cc -c $(TMS) $(TES) $(CFLAGS)
	cc $(TMO) $(TEO) -o $(TC) $(LIBS)

debug: $(TSM)	
	cc -g $(TMS) -o $(TC) $(LIBS)
	cc -g $(TES) -c $(LIBS)
clean:
	-$(RM) *.o
	-$(RM) *~
	-$(RM) \#*
	-$(RM) *.core

fclean: clean
	-$(RM) $(TC)

re: fclean all
