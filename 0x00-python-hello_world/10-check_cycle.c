#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a singly linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	hare = tortoise = list;

	if (hare == NULL || hare->next == NULL)
		return (0);
	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (hare == NULL)
			return (0);
		else if (tortoise == hare)
			break;
	}
	return (1);
}
