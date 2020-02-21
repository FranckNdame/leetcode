class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            return 0
        maxSum = currSum = sum(nums[:k])

        for i in range(k, len(nums)):
            lhs, rhs = nums[i-k], nums[i]
            currSum = currSum - lhs + rhs
            maxSum = max(maxSum, currSum)

        return maxSum/k
