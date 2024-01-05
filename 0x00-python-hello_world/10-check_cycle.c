#include "lists.h"

/**
* check_cycle - check for cycle in llist
* @list: the head of the llist
* Return: 1 if there's a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list, *hare = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (hare == tortoise)
			return (1);
	}

	return (0);
}
