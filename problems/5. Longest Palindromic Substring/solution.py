class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = [0, 0]
        for i in range(1, len(s)):
            odd = self.expandString(i-1, i+1, s)
            even = self.expandString(i-1, i, s)
            localLongest = max(odd, even, key=lambda x: x[1]-x[0])
            longest = max(longest, localLongest, key=lambda x: x[1]-x[0])
        return s[longest[0]:longest[1]]

    def expandString(self, i, j, s):
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i -= 1
            j += 1
        return [i+1, j]
