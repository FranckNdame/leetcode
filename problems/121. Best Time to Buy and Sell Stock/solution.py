class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        minPrice = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        
        return maxProfit