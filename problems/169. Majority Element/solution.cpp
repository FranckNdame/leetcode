class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        int count = 0;
        int candidate = NULL;

        for (int i = 0; i < nums.size(); i++)
        {
            if (!count)
            {
                count++;
                candidate = nums[i];
            }

            count += candidate == nums[i] ? 1 : -1;
        }

        return candidate;
    }
};