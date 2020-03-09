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
    bool hasCycle(ListNode *head)
    {
        ListNode *ptr = head;
        ListNode *runner = head;

        while (ptr && runner)
        {
            ptr = ptr->next;
            if (!runner->next)
                return false;
            runner = runner->next->next;
            if (ptr == runner)
                return true;
        }

        return false;
    }
};