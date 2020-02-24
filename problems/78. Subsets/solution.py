# Approach 1
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lookup = {}
        result = [[]]
        self.getSubsets(nums, lookup, result)
        return result

    def getSubsets(self, nums, lookup, result):
        if not nums:
            return
        if str(nums) not in lookup:
            lookup[str(nums)] = True
            result.append(nums)
        for i in range(len(nums)):
            newNums = nums[:i] + nums[i+1:]
            self.getSubsets(newNums, lookup, result)
