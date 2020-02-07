class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.helper(["(", ")"], n, result)
        return list(set(result))

    def helper(self, brackets, n, result):
        if len(brackets) == n*2:
            result.append("".join(brackets))
            return

        for i in range(len(brackets)):
            self.helper(brackets[:i] + ["("] + [")"] + brackets[i:], n, result)
