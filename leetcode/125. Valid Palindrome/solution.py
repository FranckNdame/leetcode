class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = self.formatInput(s)
        return self.checkPalindrome(arr)
    
    def checkPalindrome(self, arr):
        lhs = 0
        rhs = len(arr) - 1
        
        while lhs < rhs:
            if arr[lhs] != arr[rhs]:
                return False
            lhs += 1
            rhs -= 1
        return True
    
    def formatInput(self, s):
        arr = []
        for char in s:
            if self.isAlphabet(char):
                arr.append(char)
            elif self.isNumeric(char):
                arr.append(char)
            elif self.isCapAlphabet(char):
                arr.append(char.lower())
        return arr
        
    def isAlphabet(self, char: str) -> bool:
        return ord(char) >= 97 and ord(char) <= 122
    
    def isCapAlphabet(self, char: str) -> bool:
        return ord(char) >= 65 and ord(char) <= 90
    
    def isNumeric(self, char: str) -> bool:
        return ord(char) >= 48 and ord(char) <= 57
        