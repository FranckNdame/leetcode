# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque as queue


class Solution:
    # Recursive
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.swap(root)
        return root

    def swap(self, node):
        if not node:
            return

        node.left, node.right = node.right, node.left
        self.swap(node.right)
        self.swap(node.left)

    # Iterative

    def invertTree(self, root):
        if not root:
            return None
        q = queue([root])
        while q:
            curr = q.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root
