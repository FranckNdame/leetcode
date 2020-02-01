# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        pA, pB = 0, n-1
        
        while pA != pB:
            if knows(pA, pB): pA += 1
            else: pB -= 1
        
        for i in range(n):
            if knows(pA, i) and pA != i: return -1
            if not knows(i, pA) and pA != i: return -1
        
        return pA
        