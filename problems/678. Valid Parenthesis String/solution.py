class Solution:
    def checkValidString(self, s: str) -> bool:
        low = hi = 0
        for c in s:
            low += 1 if c == "(" else -1
            hi += 1 if c != ")" else -1
            if hi < 0:
                break
            low = max(low, 0)
        return low == 0
