class Solution:
    # First Approach
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        maxProfits = 0
        i = 0
        valley = None
        peak = None
        
        while i < len(prices)-1:
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            
            while i < len(prices)-1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            
            maxProfits += peak - valley
            
        return maxProfits
    
    
    # Approach two
    def maxProfit(self, prices: List[int]) -> int:
        maxProfits = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                maxProfits += prices[i+1] - prices[i]
        return maxProfits
    
            