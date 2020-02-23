class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if not A:
            return -1
        A.sort()
        result = -float('inf')
        left, right = 0, len(A) - 1

        while left < right:
            twoSums = A[left] + A[right]
            if twoSums < K:
                result = max(result, A[left] + A[right])
                left += 1
            else:
                right -= 1

        return -1 if result == -float('inf') else result
