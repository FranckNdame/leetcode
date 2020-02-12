class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        count = len(nums)
        start = 0

        while count:
            currIndex = start
            currVal = nums[currIndex]
            nextIndex = (currIndex + k) % len(nums)
            firstPass = True
            while True:
                if currIndex == start and not firstPass:
                    break
                firstPass = False
                temp = nums[nextIndex]
                nums[nextIndex] = currVal

                currVal = temp
                currIndex = nextIndex

                nextIndex = (currIndex + k) % len(nums)
                count -= 1
            start += 1
