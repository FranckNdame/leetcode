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
    ListNode *middleNode(ListNode *head)
    {
        ListNode *tortoise = head;
        ListNode *hare = head;

        while (true)
        {
            if (hare == nullptr || hare->next == nullptr)
                return tortoise;
            tortoise = tortoise->next;
            hare = hare->next->next;
        }
    }
};
