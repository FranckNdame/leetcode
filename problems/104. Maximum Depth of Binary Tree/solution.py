# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # Recursive
    def maxDepth(self, root: TreeNode) -> int:
        return self.getMaxDepth(root, 0)

    def getMaxDepth(self, root, maxD):
        if not root:
            return maxD
        return max(self.getMaxDepth(root.left, maxD + 1), self.getMaxDepth(root.right, maxD + 1))

    # Iterative

    def maxDepth(self, root):
        if not root:
            return 0
        maxDepth = 1
        stack = [(root, 1)]

        while stack:
            curr, currDepth = stack.pop()
            maxDepth = max(maxDepth, currDepth)

            if curr.left:
                stack.append((curr.left, currDepth + 1))
            if curr.right:
                stack.append((curr.right, currDepth + 1))
        return maxDepth
