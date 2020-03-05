class Solution
{
public:
    std::vector<int> maxSlidingWindow(std::vector<int> &nums, int k)
    {
        if (nums.size() == 0)
            return {};
        if (nums.size() == 1)
            return {nums[0]};
        int currMax;
        std::queue<int> q;
        for (int i = 0; i < k; i++)
        {
            currMax = std::max(currMax, nums[i]);
            q.push(nums[i]);
        }
        std::vector<int> result = {currMax};

        for (int i = k; i < nums.size(); i++)
        {
            int eject = q.front();
            q.pop();
            q.push(nums[i]);

            if (eject == currMax)
            {
                if (nums[i] >= currMax)
                    currMax = nums[i];
                else
                {
                    currMax = 0;
                    for (int j = i - k + 1; j < i + 1; j++)
                        currMax = std::max(currMax, nums[j]);
                }
            }
            else
            {
                currMax = std::max(currMax, nums[i]);
            }

            result.push_back(currMax);
        }

        return result;
    }
};