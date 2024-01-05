#include "lists.h"

/**
* check_cycle - check for cycle in llist
* @list: the head of the llist
* Return: 1 if there's a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *current = list, *temp;
	listint_t *visited = NULL, *bp;
	int cycle = 0;

	if (current == NULL || current->next == NULL)
		return (0);
	while (current->next != NULL)
	{
		temp = current->next;
		current->next = visited;
		visited = current;
		current = temp;

		bp = visited;
		while (bp)
		{
			if (current == bp)
			{
				cycle = 1;
				break;
			}
			bp = bp->next;
		}
		if (cycle)
			break;
	}
	bp = current;
	while (visited != NULL)
	{
		temp = visited->next;
		visited->next = bp;
		bp = visited;
		visited = temp;
	}

	return (cycle);
}
