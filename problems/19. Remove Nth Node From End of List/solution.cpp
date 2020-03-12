/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        ListNode *ptr = head;
        ListNode *runner = head;
        ListNode *prev = NULL;

        while (n)
        {
            runner = runner->next;
            n--;
        }

        while (runner != NULL)
        {
            runner = runner->next;
            prev = ptr;
            ptr = ptr->next;
        }

        if (prev == NULL)
            return head->next;
        prev->next = ptr->next;
        return head;
    }
};