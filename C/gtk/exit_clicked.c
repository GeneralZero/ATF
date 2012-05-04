//exit_clicked.c

#include "night_day.h"

gboolean exit_clicked(GtkWidget *w, gpointer data)
{
	GtkWidget *button;
	GtkWidget *popup;
	GtkWidget *label;
	GtkWidget *vbox;
	GtkWidget *hbox;
	
	popup = gtk_window_new(GTK_WINDOW_TOPLEVEL);
	
	vbox = gtk_vbox_new(FALSE, 0);
	hbox = gtk_hbox_new(FALSE, 0);
	
	label = gtk_label_new("Are you sure you want to exit?");
	gtk_widget_show(label);
	gtk_box_pack_start(GTK_BOX(vbox), label, FALSE, FALSE, 5);
	
	
	button = image_button(gtk_image_new_from_file("img/yes.png"), "Yes");
	gtk_signal_connect(GTK_OBJECT(button), "clicked", G_CALLBACK(destroy), NULL);
	gtk_box_pack_start(GTK_BOX(hbox), button, FALSE, FALSE, 5);
	gtk_widget_show(button);
		
	
	button = image_button(gtk_image_new_from_file("img/no.png"), "No");
	gtk_signal_connect(GTK_OBJECT(button), "clicked", G_CALLBACK(no_clicked), popup);
	gtk_box_pack_start(GTK_BOX(hbox), button, FALSE, FALSE, 5);
	gtk_widget_show(button);
	
	gtk_box_pack_start(GTK_BOX(vbox), hbox, FALSE, FALSE, 5);
	
	gtk_widget_show(hbox);
	gtk_widget_show(vbox);
	gtk_container_add(GTK_CONTAINER(popup), vbox);
	gtk_widget_show(popup);
	
}	
