class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper(n, {1: 1, 2: 2})

    def helper(self, n, lookup):
        if n not in lookup:
            lookup[n] = self.helper(n-1, lookup) + self.helper(n-2, lookup)
        return lookup[n]
