class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = collections.Counter(nums2)
        output = []
        for num in nums1:
            if num in counter and counter[num]:
                output.append(num)
                counter[num] -= 1
        return output
