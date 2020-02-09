class Solution:
    # Slow approach
    def canJump(self, nums: List[int]) -> bool:
        if not len(nums):
            return False
        memo = [0]*len(nums)
        memo[-1] = 1

        for i in range(len(nums)-2, -1, -1):
            futherestJump = min(i + nums[i], len(nums)-1)
            for j in range(i+1, futherestJump+1):
                if memo[j] == 1:
                    memo[i] = 1
                    break
        return memo[0] == 1

    # Optimal
    def canJump(self, nums: List[int]) -> bool:
        if not len(nums):
            return False
        lastGoodPos = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if (nums[i] + i) >= lastGoodPos:
                lastGoodPos = i
        return lastGoodPos == 0
