class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = collections.Counter(t)
        currWindow = collections.defaultdict(int)
        matchCount = len(t)
        currCount = 0
        lhs, rhs = 0, 0
        result = (float('inf'), 0, 0)

        while rhs < len(s):
            char = s[rhs]
            # print(lookup, currWindow, currCount)
            currWindow[char] += 1
            if char in lookup and currWindow[char] <= lookup[char]:
                currCount += 1

            while lhs <= rhs and matchCount == currCount:
                char = s[lhs]
                if (rhs - lhs + 1) < result[0]:
                    # print(rhs - lhs + 1)
                    result = (rhs-lhs+1, lhs, rhs)
                currWindow[char] -= 1
                if char in lookup and currWindow[char] < lookup[char]:
                    currCount -= 1
                lhs += 1
            rhs += 1

        l, r = result[1], result[2]
        return "" if result[0] == float('inf') else s[l:r+1]
