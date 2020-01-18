class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        sums = [0 for _ in nums]
        sums[0] = nums[0]
        sums[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            sums[i] = max(nums[i] + sums[i-2], sums[i-1])
        return max(sums)
