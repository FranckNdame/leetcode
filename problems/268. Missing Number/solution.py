class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n): n ^= i ^ nums[i]
        return n        