class Solution:
    # Time Complexity: O(n) || Space complexity: O(1)
    def removeDuplicates(self, nums: [int]) -> int:
        insertionIndex = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[insertionIndex] = nums[i+1]
                insertionIndex += 1
        return insertionIndex


solution = Solution()
print(solution.removeDuplicates([1, 1, 3, 4, 4, 6, 7, 8]))
