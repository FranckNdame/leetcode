class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertionIndex = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[insertionIndex-2] or nums[i] != nums[insertionIndex-1]:
                nums[insertionIndex] = nums[i]
                insertionIndex += 1
        return insertionIndex
