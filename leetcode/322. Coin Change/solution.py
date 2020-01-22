class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [float('inf') for _ in range(amount+1)]
        minCoins[0] = 0
        
        for coin in coins:
            for i in range(coin, amount+1):
                    minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)
        return minCoins[amount] if minCoins[amount] != float('inf') else -1
        
        