class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        result = set()
        while i < len(nums) - 2:
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                potentialTriplet = nums[i] + nums[j] + nums[k]
                if potentialTriplet == 0:
                    result.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                if potentialTriplet > 0:
                    k -= 1
                if potentialTriplet < 0:
                    j += 1
            i += 1

        return list(result)
