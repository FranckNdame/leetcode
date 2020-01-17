class Solution:
    # Time Complexity: O(n) || Space Complexity: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        lookup = {}
        threshold = len(nums) // 2
        for num in nums:
            if num in lookup:
                lookup[num] += 1
                if lookup[num] > threshold:
                    return num
            else:
                lookup[num] = 1

        return max(lookup, key=lookup.get)

    # Time Complexity: O(n) || Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate
