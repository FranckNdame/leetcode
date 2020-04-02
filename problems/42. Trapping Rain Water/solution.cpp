class Solution
{
public:
    int trap(vector<int> &height)
    {
        if (height.empty())
            return 0;
        int result(0), lMax(0);
        vector<int> rMax(height.size(), 0);
        rMax[rMax.size() - 1] = height[height.size() - 1];
        for (int i = height.size() - 2; i >= 0; i--)
            rMax[i] = max(height[i], rMax[i + 1]);
        for (int i = 0; i < height.size(); i++)
        {
            lMax = max(height[i], lMax);
            result += min(rMax[i], lMax) - height[i];
        }
        return result;
    }
};
