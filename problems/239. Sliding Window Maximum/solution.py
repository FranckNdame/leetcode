class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        queue = collections.deque(nums[:k])
        currMax = max(nums[:k])
        result = [currMax]
        for i in range(k, len(nums)):
            eject = queue.popleft()
            queue.append(nums[i])
            if eject == currMax:
                if (nums[i] >= currMax):
                    currMax = nums[i]
                else:
                    currMax = max(nums[i-k+1:i+1])
            else:
                currMax = max(currMax, nums[i])

            result.append(currMax)
        return result
