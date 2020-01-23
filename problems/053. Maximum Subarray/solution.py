class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currentSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(maxSum, currentSum)
        return maxSum
        