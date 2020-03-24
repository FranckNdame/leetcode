class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] > 0)
                break;
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            int left = i + 1, right = nums.size() - 1;
            while (left < right)
            {
                int triplets = nums[i] + nums[left] + nums[right];
                if (triplets > 0)
                    right--;
                else if (triplets < 0)
                    left++;
                else
                {
                    result.push_back(vector<int>({nums[i], nums[left], nums[right]}));
                    while (left < right && nums[left] == nums[left + 1])
                        left++;
                    while (left < right && nums[right] == nums[right - 1])
                        right--;
                    left++;
                    right--;
                }
            }
        }

        return result;
    }
};