class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(n, result)
        return result

    def backtrack(self, n, result, string="", left=0, right=0):
        if len(string) == n*2:
            result.append(string)
        if left < n:
            self.backtrack(n, result, string + "(", left+1, right)
        if right < left:
            self.backtrack(n, result, string + ")", left, right+1)
