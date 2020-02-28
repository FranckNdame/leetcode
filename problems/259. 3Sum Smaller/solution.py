class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        
        for i in range(len(nums)):
            j, k = i+1, len(nums) - 1
            while j < k:
                triplet = nums[i] + nums[j] + nums[k]
                if triplet < target: 
                    count += (k - j)
                    j += 1
                else: 
                    k -= 1
        
        return count
