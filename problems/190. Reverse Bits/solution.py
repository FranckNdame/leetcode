class Solution:
    def reverseBits(self, n: int) -> int:
        reversedBits = format(n, "032b")[::-1]
        return int(reversedBits, 2)
