class Solution:
    # Time Complexity: O(n) || Space complexity: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        insertionIndex = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[insertionIndex] = nums[i+1]
                insertionIndex += 1
        return insertionIndex