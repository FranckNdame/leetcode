class Solution:
    
    def moveZeroes(self, nums):
        slot = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[slot] = nums[i]
                slot += 1
        for j in range(slot, len(nums)):
            nums[j] = 0