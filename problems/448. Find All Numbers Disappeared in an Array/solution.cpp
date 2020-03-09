class Solution
{
public:
    vector<int> findDisappearedNumbers(vector<int> &nums)
    {
        vector<int> result;
        for (int i = 0; i < nums.size(); i++)
        {
            int k = abs(nums[i]) - 1;
            if (nums[k] > 0)
                nums[k] *= -1;
        }

        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] > 0)
                result.push_back(i + 1);
        }

        return result;
    }
};