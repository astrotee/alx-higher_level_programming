#include "lists.h"
#include <stdlib.h>

/**
* is_palindrome - check if llist is a palindrome
* @head: double pointer to the head of llist
* Return: 1 if is a palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	int palindrome = 1;
	int size = 0;
	int i;
	listint_t *revlist;
	listint_t *prev = NULL;
	listint_t *new;
	listint_t *current = *head;

	while (current)
	{
		size++;
		new = malloc(sizeof(listint_t));
		new->n = current->n;
		new->next = prev;
		prev = new;
		revlist = new;
		current = current->next;
	}

	current = *head;

	for (i = 0; i < size; i++)
	{
		if (palindrome && current->n != revlist->n)
			palindrome = 0;

		current = current->next;
		prev = revlist;
		revlist = revlist->next;
		free(prev);
	}


	return (palindrome);
}
