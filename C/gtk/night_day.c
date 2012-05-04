//night_day.c

#include "night_day.h"

int main (int argc, char** argv)
{
	GtkWidget *window;
	GtkWidget *button;
	GtkWidget *vbox;
	GtkWidget *hbox;

	gtk_init (&argc, &argv);

	window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
	gtk_window_set_title (GTK_WINDOW (window), "Day & Night");
	gtk_signal_connect(GTK_OBJECT(window), "delete_event", G_CALLBACK(close_clicked), NULL);
	gtk_container_border_width(GTK_CONTAINER(window), 10);

	vbox = gtk_vbox_new(FALSE, 0);
	hbox = gtk_hbox_new(FALSE, 0);

	button = image_button(gtk_image_new_from_file("img/sun.gif"), "Day");
	gtk_signal_connect(GTK_OBJECT(button), "clicked", G_CALLBACK(day_clicked), NULL);
	gtk_box_pack_start(GTK_BOX(hbox), button, FALSE, FALSE, 5);
	gtk_widget_show(button);
	
	
	button = image_button(gtk_image_new_from_file("img/moon.png"), "Night");
	gtk_signal_connect(GTK_OBJECT(button), "clicked", G_CALLBACK(night_clicked), NULL);
	gtk_box_pack_start(GTK_BOX(hbox), button, FALSE, FALSE, 5);
	gtk_widget_show(button);
	
	gtk_box_pack_start(GTK_BOX(vbox), hbox, FALSE, FALSE, 5);
	gtk_widget_show(hbox);
	
	
	button = image_button(gtk_image_new_from_file("img/exit.jpg"), "Exit");
	gtk_signal_connect(GTK_OBJECT(button), "clicked", G_CALLBACK(exit_clicked), NULL);
	gtk_box_pack_start(GTK_BOX(vbox), button, FALSE, FALSE, 5);
	gtk_widget_show(button);
	
		
	gtk_widget_show(vbox);
	gtk_container_add(GTK_CONTAINER(window), vbox);
	gtk_widget_show(window);

	gtk_main();
	return 0;
}
