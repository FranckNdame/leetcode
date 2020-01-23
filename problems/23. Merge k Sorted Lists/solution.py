# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop


class Solution:
    def mergeKLists(self, lists: [ListNode]):

        heap = []
        for l in lists:
            if l:
                heappush(heap, (l.val, id(l), l))

        head = curr = ListNode(None)

        while heap:
            val, nodeId, node = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next

            if node:
                heappush(heap, (node.val, id(node), node))

        return head.next
