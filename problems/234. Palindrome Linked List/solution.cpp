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
    bool isPalindrome(ListNode *head)
    {
        ListNode *mid = head;
        ListNode *runner = head;

        while (runner)
        {
            mid = mid->next;
            if (!runner->next)
                break;
            runner = runner->next->next;
        }

        mid = reverse(mid);
        ListNode *left = head;
        ListNode *right = mid;

        while (right)
        {
            if (left->val != right->val)
                return false;
            left = left->next;
            right = right->next;
        }

        return true;
    }

    ListNode *reverse(ListNode *node)
    {
        if (!node || !node->next)
            return node;
        ListNode *p = reverse(node->next);
        node->next->next = node;
        node->next = NULL;
        return p;
    }
};