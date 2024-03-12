#include <stdio.h>
#include <stdlib.h>
#include <lists.h>

/**
 * check_cycle - check if there is a cycle in list
 * @list: pointer to list
 * Return: 1 if find cycle, 0 if otherwise
 */

int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
		return(0);
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		
		if(slow == fast)
			return(1);
	}
	return(0);
}
