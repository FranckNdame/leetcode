class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        int cost = 0;
        for (long i = nums.size() - 2; i >= 0; i--)
        {
            cost++;
            if (nums[i] >= cost)
                cost = 0;
        }

        return cost == 0;
    }
};