class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -1 * abs(nums[index])

        for j in range(len(nums)):
            if nums[j] > 0:
                result.append(j+1)
        return result
