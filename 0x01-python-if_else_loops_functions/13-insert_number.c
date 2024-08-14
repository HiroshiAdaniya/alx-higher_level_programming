#include "lists.h"
/**
 * insert_node - inserts a number into a sorted linked list
 * @head: head of a linked list
 * @number: an integer to add to the list
 * Return: The address of the newnode, else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = NULL;
	listint_t *start = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;

	if (start == NULL)
		*head = newnode;
	else if (newnode->n <= start->n)
	{
		newnode->next = start;
		*head = newnode;
	}
	else
	{
		while (start->next != NULL && start->next->n < newnode->n)
			start = start->next;
		newnode->next = start->next;
		start->next = newnode;
	}
	return (newnode);
}
