class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        left, right = 0, len(numbers) - 1
        while left < right:
            twoSum = numbers[left] + numbers[right]
            if twoSum == target:
                return [left+1, right+1]
            elif twoSum > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]
