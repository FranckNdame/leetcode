class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        longest = ""
        for i in range(1,len(s)):
            odd = self.expandString(i-1, i+1, s)
            even = self.expandString(i-1, i, s)
            localLongest = max(odd, even, key=lambda x:len(x))
            longest = max(longest, localLongest, key=lambda x:len(x))
        return longest
            
            
    def expandString(self, i, j, s):
        while i >= 0 and j < len(s):
            if s[i] != s[j]: break
            i -= 1
            j += 1
        return  s[i+1:j]
        