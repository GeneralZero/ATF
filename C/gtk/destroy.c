//destroy.c

#include "night_day.h"

gboolean destroy(GtkWidget *w, gpointer data)
{
	gtk_main_quit();
	return TRUE;
}
