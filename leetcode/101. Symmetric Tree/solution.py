# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque as queue


class Solution:
    # Time complexity: O(N) || Space Complexity: O(N)
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, leftNode, rightNode):
        # Base case
        if not leftNode and not rightNode:
            return True
        if not leftNode or not rightNode:
            return False

        cond1 = leftNode.val == rightNode.val
        cond2 = self.isMirror(leftNode.left, rightNode.right)
        cond3 = self.isMirror(leftNode.right, rightNode.left)

        return cond1 and cond2 and cond3


#     # Iterative


    def isSymmetric2(self, root) -> bool:
        q = queue([root, root])

        while q:
            leftNode = q.popleft()
            rightNode = q.popleft()

            if not leftNode and not rightNode:
                continue
            if not leftNode or not rightNode:
                return False
            if leftNode.val != rightNode.val:
                return False

            q.append(leftNode.left)
            q.append(rightNode.right)
            q.append(leftNode.right)
            q.append(rightNode.left)

        return True
