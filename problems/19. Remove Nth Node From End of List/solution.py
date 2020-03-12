# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # Approach one
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        offset = 1
        pointer, runner = head, head

        while offset < n:
            runner = runner.next

        while runner.next:
            runner = runner.next
            pointer = pointer.next

        pointer.val = pointer.next.val
        pointer.next = pointer.next.next

        return head

    # Approach two

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        offset = 1
        pointer, runner, prev = head, head, None

        while offset < n:
            runner = runner.next

        while runner.next:
            runner = runner.next
            prev = pointer
            pointer = pointer.next

        prev.next = pointer.next

        return head
