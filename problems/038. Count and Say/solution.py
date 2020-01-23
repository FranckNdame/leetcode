class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"

        sequence = self.countAndSay(n-1)
        i = 0
        j = 1
        count = 1
        result = []

        # construct new sequence
        while i < len(sequence):
            while j < len(sequence) and sequence[i] == sequence[j]:
                count += 1
                j += 1
            result.extend([str(count), str(sequence[i])])
            i = j
            j += 1
            count = 1

        return "".join(result)
