class Solution
{
public:
    int maxProfit(vector<int> &prices, int fee)
    {
        if (prices.size() < 2)
            return 0;
        int canBuy(0), canSell(-prices[0]), tempCanBuy(0);
        for (int i = 0; i < prices.size(); i++)
        {
            tempCanBuy = canBuy;
            canBuy = max(canBuy, canSell + prices[i] - fee);
            canSell = max(canSell, tempCanBuy - prices[i]);
        }
        return canBuy;
    }
};