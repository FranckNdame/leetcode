class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {num: True for num in nums1}
        result = []
        for num in nums2:
            if num in lookup and lookup[num]:
                result.append(num)
                lookup[num] = False
        return result
