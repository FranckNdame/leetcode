class Solution:
    def isHappy(self, n: int) -> bool:
        lookup = {}
        while n != 1:
            if n in lookup:
                return False
            lookup[n] = True
            n = self.getDigitsSquare(n)
        return True

    def getDigitsSquare(self, n):
        temp = 0
        while n > 0:
            temp += (n % 10)**2
            n = n // 10
        return temp
