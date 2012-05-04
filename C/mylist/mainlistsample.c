#include "../lib/mylist.h"

int main()
{
  int arr[10] = {4, 65, 32, 1, 68, 23, 83, 12, 6, 82};
  node *head;
  int i;
  int n;

  n=10;
  head = NULL;
  for (i = 0; i < 5; i++)
    add_node(new_node(&arr[i], NULL), &head);
  traverse_int(head);
  for (; i < 10; i++)
    add_elem(&arr[i], &head);
  traverse_int(head);
  my_char('\n');
  n = 5;
  add_node_at(new_node(&n, NULL), &head, 2);
  traverse_int(head);
  my_char('\n');
  add_node(new_node(&n, NULL), &head);
  //traverse_int(head);
  my_char('\n');
  add_node_at(new_node(&n, NULL), &head, 0);
  traverse_int(head);
  add_node_at(new_node(&n, NULL), &head, 34);
  append(new_node(&n, NULL), &head);
  remove_node(&head);
  traverse_int(head);
  my_char('\n');
  remove_node_at(&head, 4);
  traverse_int(head);
  my_char('\n');
  remove_node_at(&head, 0);
  remove_node_at(&head, 35);
  traverse_int(head);
  my_char('\n');
  remove_last(&head);
  traverse_int(head);
  my_char('\n');
  my_int(count_nodes(head));
  my_char('\n');
  empty_list(&head);
  traverse_int(head);
  return 0;
}
