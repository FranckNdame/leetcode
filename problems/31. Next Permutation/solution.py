class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        j = len(nums) - 1
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])
