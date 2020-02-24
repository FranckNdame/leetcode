class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = sum = 0
        lookup = {0: 1}

        for num in nums:
            sum += num
            if (sum - k) in lookup:
                count += lookup[sum-k]
            if sum in lookup:
                lookup[sum] += 1
            else:
                lookup[sum] = 1

        return count
