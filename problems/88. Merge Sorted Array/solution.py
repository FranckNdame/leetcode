class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums1 or not nums2: return 
        pointer1 = m - 1
        pointer2 = n - 1
        slot = len(nums1) - 1
        
        while slot >= 0 and pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] >= nums2[pointer2]:
                nums1[pointer1], nums1[slot] = nums1[slot], nums1[pointer1]
                slot -= 1
                pointer1 -= 1
            else:
                nums2[pointer2], nums1[slot] = nums1[slot], nums2[pointer2]
                slot -= 1
                pointer2 -= 1
        
        while slot >= 0 and pointer1 >= 0:
            nums1[pointer1], nums1[slot] = nums1[slot], nums1[pointer1]
            slot -= 1
            pointer1 -= 1
            
        while slot >= 0 and pointer2 >= 0:
            nums2[pointer2], nums1[slot] = nums1[slot], nums2[pointer2]
            slot -= 1
            pointer2 -= 1
        
        return nums1