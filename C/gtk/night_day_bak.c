//night_day.c

#include "night_day.h"

gboolean night(GtkWidget *w, gpointer data)
{
	gtk_main_quit();
}

gboolean exit_clicked(GtkWidget *w, gpointer data)
{
	//gtk_main_quit();
	g_print("Good Bye\n");
}

gboolean day(GtkWidget *w, gpointer data)
{
	g_print("Hi\n");
}


int main (int argc, char** argv)
{
	GtkWidget *window;
	GtkWidget *button;

	gtk_init (&argc, &argv);

	window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
	gtk_signal_connect(GTK_OBJECT(window), "destroy", G_CALLBACK(destroy), NULL);
	gtk_container_border_width(GTK_CONTAINER(window), 10);
	
	hbox = gtk_hbox_new(FALSE, 0);

	button = gtk_button_new_with_label("Hello World");

	gtk_signal_connect(GTK_OBJECT(button), "clicked", G_CALLBACK(night), NULL);
	gtk_container_add(GTK_CONTAINER(window), button);

	gtk_widget_show(button);
	gtk_widget_show(window);

	gtk_main();
	return 0;
}
