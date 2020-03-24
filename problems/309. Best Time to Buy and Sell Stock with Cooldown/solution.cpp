class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        if (prices.size() < 2)
            return 0;
        int canBuy(0), canSell(-prices[0]), coolDown(INT_MIN);
        for (int i = 0; i < prices.size(); i++)
        {
            int tempCanSell(canSell), tempCanBuy(canBuy);
            canBuy = max(canBuy, coolDown);
            canSell = max(canSell, tempCanBuy - prices[i]);
            coolDown = tempCanSell + prices[i];
        }

        return max(canBuy, coolDown);
    }