class Solution
{
public:
    // Counting sort
    void sortColors(vector<int> &nums)
    {
        unordered_map<int, int> count{{0, 0}, {1, 0}, {2, 0}};
        for (int num : nums)
            count[num]++;
        int currColor = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            while (!count[currColor])
                currColor++;
            nums[i] = currColor;
            count[currColor]--;
        }
    }

    // One pass
    void sortColors(vector<int> &nums)
    {
        int pivot = 1, smaller = 0, equal = 0, greater = nums.size() - 1;
        while (equal <= greater)
        {
            if (nums[equal] == pivot)
                equal++;
            else if (nums[equal] > pivot)
                swap(nums[equal], nums[greater--]);
            else
                swap(nums[equal++], nums[smaller++]);
        }
    }
};