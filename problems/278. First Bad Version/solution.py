# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        left, right = 0, n-1

        while left <= right:
            m = (left+right)//2
            if isBadVersion(m+1):
                if not isBadVersion(m):
                    return m+1
                right = m - 1
            else:
                left = m + 1
