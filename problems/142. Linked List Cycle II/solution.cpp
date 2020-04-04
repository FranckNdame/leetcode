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
    ListNode *detectCycle(ListNode *head)
    {
        if (head == nullptr)
            return nullptr;
        ListNode *tortoise = head;
        ListNode *hare = head;
        while (true)
        {
            tortoise = tortoise->next;
            if (hare == nullptr || hare->next == nullptr)
                return NULL;
            hare = hare->next->next;
            if (hare == tortoise)
                break;
        }

        ListNode *ptr1 = head;
        ListNode *ptr2 = hare;

        while (ptr1 != ptr2)
        {
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }

        return ptr1;
    }
};
