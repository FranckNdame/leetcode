class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if haystack == needle:
            return 0
        if len(needle) >= len(haystack):
            return -1

        prefix_table = self.constructTable(needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = prefix_table[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1

        return -1

    def constructTable(self, pattern: str) -> [int]:
        table = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = table[j-1]
            if pattern[i] == pattern[j]:
                j += 1
            table[i] = j
        return table
