class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = collections.Counter(text)
        result = float('inf')

        for char in "ban":
            result = min(result, count[char])

        for char in "lo":
            result = min(result, count[char]//2)

        return 0 if result == float('inf') else result
