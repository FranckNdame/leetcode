# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node, minVal, maxVal):
        if not node:
            return True
        if node.val <= minVal or node.val >= maxVal:
            return False
        if not self.helper(node.left, minVal, node.val):
            return False
        if not self.helper(node.right, node.val, maxVal):
            return False

        return True
