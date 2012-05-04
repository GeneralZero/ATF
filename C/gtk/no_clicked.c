//no_clicked.c

#include "night_day.h"

gboolean no_clicked(GtkWidget *b, gpointer w)
{
	gtk_widget_destroy((GtkWidget*)w);
}

