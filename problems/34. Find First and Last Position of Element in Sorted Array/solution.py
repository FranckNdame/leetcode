class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        left, right = 0, len(nums)-1

        result[0] = self.getExtremities(nums, target, "left")
        if result[0] == -1:
            return result
        result[1] = self.getExtremities(nums, target, "right")

        return result

    def getExtremities(self, nums, target, direction):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                if direction == "left":
                    if mid > 0 and nums[mid] == nums[mid-1]:
                        right = mid - 1
                    else:
                        return mid
                else:
                    if mid < len(nums)-1 and nums[mid] == nums[mid+1]:
                        left = mid + 1
                    else:
                        return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid + 1
        return -1
