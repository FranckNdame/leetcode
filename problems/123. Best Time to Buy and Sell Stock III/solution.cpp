class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        if (prices.size() < 2)
            return 0;
        int canBuy(0), canBuyTwo(0), canSell(-prices[0]), canSellTwo(INT_MIN);
        int canBuyTemp(0);
        for (int price : prices)
        {
            canBuyTemp = canBuy;
            canBuy = max(canBuy, canSell + price);
            canSell = max(canSell, -price);
            canBuyTwo = max(canBuyTwo, canSellTwo + price);
            canSellTwo = max(canSellTwo, canBuyTemp - price);
        }

        return canBuyTwo;
    }
};