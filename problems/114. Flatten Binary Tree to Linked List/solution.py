# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        curr = root
        stack = []
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

        while stack:
            nextNode = stack.pop()
            curr.left = None
            curr.right = nextNode

            if nextNode.right:
                stack.append(nextNode.right)
            if nextNode.left:
                stack.append(nextNode.left)

            curr = nextNode
