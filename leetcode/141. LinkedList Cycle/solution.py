# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # Time Complexity: O(n) || Space Complexity: O(n)
    def hasCycle(self, head: ListNode) -> bool:
        lookup = {}
        pos = 0
        curr = head

        while curr:
            if curr in lookup:
                return True
            else:
                lookup[curr] = pos

            curr = curr.next
            pos += 1

        return False

    # Time Complexity: O(n) || Space Complexity: O(1)
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        pointer = head
        runner = head.next

        while pointer and runner:
            if pointer == runner:
                return True
            pointer = pointer.next

            if not runner.next:
                return False
            else:
                runner = runner.next.next

        return False
