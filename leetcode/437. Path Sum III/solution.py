# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.result = 0

        def depthFirstSearch(node, target):
            if not node:
                return
            if node.val == target:
                self.result += 1
            depthFirstSearch(node.left, target - node.val)
            depthFirstSearch(node.right, target - node.val)

        def traverse(node, target):
            if not node:
                return
            depthFirstSearch(node, target)
            traverse(node.left, target)
            traverse(node.right, target)

        traverse(root, sum)

        return self.result
