#ifndef NIGHT_DAY_H_
#define NIGHT_DAY_H_

#include <gtk/gtk.h>

#ifndef NULL
#define NULL ((void*)0)
#endif

gboolean night_clicked(GtkWidget*, gpointer);
gboolean destroy(GtkWidget*, gpointer);
gboolean close_clicked(GtkWidget*, gpointer);
gboolean day_clicked(GtkWidget*, gpointer);
gboolean exit_clicked(GtkWidget*, gpointer);
gboolean no_clicked(GtkWidget*, gpointer);
GtkWidget* image_button(GtkWidget*, char*);

#endif
