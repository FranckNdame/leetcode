class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                triplet = nums[i] + nums[j] + nums[k]
                if triplet == target:
                    return triplet

                if abs(triplet-target) < abs(closest-target):
                    closest = triplet

                if target > triplet:
                    j += 1
                else:
                    k -= 1

        return closest
