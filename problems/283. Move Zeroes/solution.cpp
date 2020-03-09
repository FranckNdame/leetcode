class Solution
{
public:
    void moveZeroes(vector<int> &nums)
    {
        int slot = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i])
            {
                swap(slot, i, nums);
                slot++;
            }
        }
    }

    void swap(int i, int j, vector<int> &array)
    {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
};