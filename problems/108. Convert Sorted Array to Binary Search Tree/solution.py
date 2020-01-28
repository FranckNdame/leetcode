# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return
        return self.binarySearch(nums, 0, len(nums) - 1)
    
    
    def binarySearch(self, nums, lhs, rhs):
        if lhs > rhs: return None
        mid = (lhs + rhs) // 2
        root = TreeNode(nums[mid])
        root.left = self.binarySearch(nums, lhs, mid-1)
        root.right = self.binarySearch(nums, mid+1, rhs)
        
        return root
        