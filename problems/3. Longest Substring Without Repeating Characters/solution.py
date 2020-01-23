class Solution:

    # Time complexity: O(n) || Space complexity: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        lookup = {}
        startIndex = 0
        result = [0, 0]

        for i in range(len(s)):
            if s[i] in lookup:
                startIndex = max(startIndex, lookup[s[i]] + 1)
                lookup[s[i]] = i
            else:
                lookup[s[i]] = i

            if (i - startIndex) > (result[1] - result[0]):
                result = [startIndex, i]

        return (result[1] - result[0]) + 1
