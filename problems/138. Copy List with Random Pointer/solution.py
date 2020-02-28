"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visits = {}
        return self.helper(head, visits)

    def helper(self, node, visits):
        if not node:
            return
        if node in visits:
            return visits[node]
        newNode = Node(node.val)
        visits[node] = newNode
        newNode.next = self.helper(node.next, visits)
        newNode.random = self.helper(node.random, visits)

        return newNode
