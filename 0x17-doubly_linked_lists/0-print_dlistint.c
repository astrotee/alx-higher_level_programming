#include <stdio.h>
#include "lists.h"

/**
* print_dlistint - print a dlist
* @h: head pointer
* Return: the size of the list
*/
size_t print_dlistint(const dlistint_t *h)
{
	size_t size = 0;

	while (h)
	{
		printf("%d\n", h->n);
		size++;
		h = h->next;
	}

	return (size);
}
