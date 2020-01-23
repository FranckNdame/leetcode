class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = {}

        for i in range(len(s)):
            if s[i] in lookup:
                lookup[s[i]] += 1
            else:
                lookup[s[i]] = 1

        for index, char in enumerate(s):
            if lookup[char] == 1:
                return index

        return -1
