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
    // Iterative
    ListNode *reverseList(ListNode *head)
    {
        if (!head)
            return NULL;
        ListNode *prev = NULL;
        ListNode *curr = head;
        ListNode *next = curr->next;

        while (true)
        {
            curr->next = prev;
            if (!next)
                break;
            prev = curr;
            curr = next;
            next = next->next;
        }

        return curr;
    }

    // Recursive
    ListNode *reverseList(ListNode *head)
    {
        if (!head || !head->next)
            return head;
        ListNode *node = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return node;
    }
};