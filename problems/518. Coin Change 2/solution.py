class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        combinations = [0 for i in range(amount+1)]
        combinations[0] = 1
        for coin in coins:
            for i in range(1, amount+1):
                if i < coin:
                    continue
                combinations[i] += combinations[i-coin]
        return combinations[amount]
