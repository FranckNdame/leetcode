class Solution:
    Time Complexity: O(n) || Space Complexity: O(1)
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = self.stripRightIndex(s)
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1
        return count
    
    def stripRightIndex(self, s):
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        return i
        
