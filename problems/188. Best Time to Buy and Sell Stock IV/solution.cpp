class Solution
{
public:
    int maxProfit(int k, vector<int> &prices)
    {
        if (prices.size() < 2)
            return 0;
        if (k < 1)
            return 0;
        if (k > prices.size() / 2)
        {
            int profit = 0;
            for (int i = 1; i < prices.size(); i++)
            {
                profit += max(prices[i] - prices[i - 1], 0);
            }
            return profit;
        }
        vector<int> canBuy(k, 0), canSell(k, -prices[0]);
        int temp(0);
        for (int i = 1; i < prices.size(); i++)
        {
            for (int j = 0; j < k; j++)
            {
                temp = j > 0 ? canBuy[j - 1] : 0;
                canBuy[j] = max(canBuy[j], canSell[j] + prices[i]);
                canSell[j] = max(canSell[j], temp - prices[i]);
            }
        }
        return canBuy.back();
    }
};