# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # Iterative Solution: 28ms (95.37%) || 12.8 mb (100%)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l1

        root = ListNode(0)
        curr = root

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next

        if not l1:
            curr.next = l2
        if not l2:
            curr.next = l1

        return root.next

    # Recursive Solution: 36ms (53.54%) || 12.8 mb (100%)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            node = ListNode(l1.val)
            node.next = self.mergeTwoLists(l1.next, l2)
        else:
            node = ListNode(l2.val)
            node.next = self.mergeTwoLists(l1, l2.next)

        return node
