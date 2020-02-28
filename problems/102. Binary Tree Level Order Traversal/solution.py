# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = [[root.val]]
        self.traverse(root, 1, result)
        return result

    def traverse(self, node, level, result):
        if not node:
            return
        if not node.left and not node.right:
            return
        arr = [] if len(result) - 1 < level else result[level]
        if node.left:
            arr.append(node.left.val)
        if node.right:
            arr.append(node.right.val)
        if len(result) - 1 < level:
            result.append(arr)

        self.traverse(node.left, level+1, result)
        self.traverse(node.right, level+1, result)
