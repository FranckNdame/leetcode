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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        int count = 2;
        ListNode *currA = headA;
        ListNode *currB = headB;
        while (count >= 0 && (currA != currB))
        {
            currA = currA ? currA->next : headB;
            currB = currB ? currB->next : headA;
            if (currA == headB || currB == headA)
                count--;
        }

        return currA;
    }
};