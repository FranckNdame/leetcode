class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> lookup;
        for (int i = 0; i < nums.size(); i++)
        {
            int otherPair = target - nums[i];
            if (lookup.find(otherPair) != lookup.end() && lookup[otherPair] != i)
                return {lookup[otherPair], i};
            lookup[nums[i]] = i;
        }

        return {-1, -1};
    }
};
