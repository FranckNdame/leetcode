# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # Iterative
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        curr = head
        next_ = head.next

        while curr.next:
            curr.next = prev
            # update pointers
            prev = curr
            curr = next_
            next_ = curr.next
        curr.next = prev

        return curr

    # Recursive
    def reverseList(self, head: ListNode):
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return node
