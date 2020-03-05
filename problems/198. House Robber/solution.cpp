
class Solution
{
public:
    int rob(vector<int> &nums)
    {
        if (nums.size() == 0)
            return 0;
        if (nums.size() == 1)
            return nums[0];
        std::vector<int> result(nums.size());
        result[0] = nums[0];
        result[1] = std::max(nums[0], nums[1]);

        for (int i = 2; i < nums.size(); i++)
        {
            result[i] = std::max(nums[i] + result[i - 2], result[i - 1]);
        }
        std::vector<int>::iterator it;
        it = max_element(result.begin(), result.end());
        return *it;
    }
};