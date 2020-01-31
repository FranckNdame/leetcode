class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        x, y = 0, 0
        
        for i in range(len(nums)+1): x ^= i
        for num in nums: y ^= num
            
        return x^y
        