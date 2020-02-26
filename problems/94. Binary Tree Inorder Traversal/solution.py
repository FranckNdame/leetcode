# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # Recursive
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, node, result):
        if not node:
            return
        self.traverse(node.left, result)
        result.append(node.val)
        self.traverse(node.right, result)

    # Iterative
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        curr = root
        stack = []
        result = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result
