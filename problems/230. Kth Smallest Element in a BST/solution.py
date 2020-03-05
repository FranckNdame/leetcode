# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inOrder = []
        self.getElements(root, inOrder)
        return inOrder[k-1]

    def getElements(self, node, arr):
        if not node:
            return
        self.getElements(node.left, arr)
        arr.append(node.val)
        self.getElements(node.right, arr)
