class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        if (nums.size() < 2)
            return nums;
        vector<int> leftProd(nums.size(), 1), rightProd(nums.size(), 1);
        int leftCurr = 1, rightCurr = 1;

        for (int i = 0; i < nums.size(); i++)
        {
            leftCurr *= nums[i];
            rightCurr *= nums[nums.size() - i - 1];
            leftProd[i] = leftCurr;
            rightProd[nums.size() - i - 1] = rightCurr;
        }

        nums[0] = rightProd[1];
        nums[nums.size() - 1] = leftProd[nums.size() - 2];
        for (int i = 1; i < nums.size() - 1; i++)
        {
            nums[i] = leftProd[i - 1] * rightProd[i + 1];
        }

        return nums;
    }
};
