class Solution
{
public:
    int subarraySum(vector<int> &nums, int k)
    {
        int count(0), sum(0);
        unordered_map<int, int> hash({{0, 1}});
        for (int num : nums)
        {
            sum += num;
            if (hash.find(sum - k) != hash.end())
                count += hash[sum - k];
            hash[sum] += 1;
        }
        return count;
    }
};