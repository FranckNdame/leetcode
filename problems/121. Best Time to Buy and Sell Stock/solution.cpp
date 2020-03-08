class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        if (prices.size() == 0)
            return 0;
        int minPrice = prices[0];
        int maxProfit = 0;
        for (int i = 1; i < prices.size(); i++)
        {
            minPrice = min(minPrice, prices[i]);
            maxProfit = max(maxProfit, prices[i] - minPrice);
        }

        return maxProfit;
    }
};
