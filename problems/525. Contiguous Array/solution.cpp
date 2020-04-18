class Solution
{

public:
    int findMaxLength(vector<int> &nums)
    {
        int maxLen(0), count(0);
        unordered_map<int, int> map;

        for (int i = 0; i < nums.size(); i++)
        {
            count += (nums[i] == 1) ? 1 : -1;
            if (count == 0)
                maxLen = max(maxLen, i + 1);
            else
            {
                if (map.find(count) != map.end())
                {
                    maxLen = max(maxLen, i - map[count]);
                }
                else
                    map[count] = i;
            }
        }

        return maxLen;
    }
};
