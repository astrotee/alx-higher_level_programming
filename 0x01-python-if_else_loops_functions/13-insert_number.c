#include "lists.h"
#include <stdlib.h>

/**
* insert_node - insert a node in ordered llist
* @head: the head pointer
* @number: the number to insert
* Return: the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (current == NULL)
		*head = new;
	else if (current->n > number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current->n < number && current->next != NULL)
		{
			if (current->next->n > number)
				break;
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
