//image_button.c

#include "night_day.h"

GtkWidget* image_button(GtkWidget* image, char* label_txt)
{
	GtkWidget *button;
	GtkWidget *label;
	GtkWidget *bbox;

	bbox = gtk_hbox_new(FALSE, 0);

	button = gtk_button_new();
	label = gtk_label_new(label_txt);
	gtk_box_pack_start(GTK_BOX(bbox), image, FALSE, FALSE, 5);
	gtk_box_pack_start(GTK_BOX(bbox), label, FALSE, FALSE, 5);
	gtk_container_add(GTK_CONTAINER(button), bbox);
	gtk_widget_show(bbox);
	gtk_widget_show(image);
	gtk_widget_show(label);
	
	return button;
}
