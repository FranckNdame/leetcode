class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        i = len(digits) - 1
        digits[i] += 1

        while i > 0 and digits[i] > 9:
            digits[i] = 0
            digits[i-1] += 1
            i -= 1

        if digits[i] > 9:
            digits[i] = 0
            digits.append(1)
            digits[i], digits[-1] = digits[-1], digits[i]

        return digits
