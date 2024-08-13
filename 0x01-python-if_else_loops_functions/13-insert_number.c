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
	listint_t *tmp = start;

	if (*head == NULL)
		return (NULL);

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	if (start->n >= newnode->n)
	{
		newnode->next = start;
		start = newnode;
	}
	else
	{
		while (tmp->next != NULL && tmp->next->n < newnode->n)
			tmp = tmp->next;
		newnode->next = tmp->next;
		tmp->next = newnode;
	}
	return (newnode);
}
