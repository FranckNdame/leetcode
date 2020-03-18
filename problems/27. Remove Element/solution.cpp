class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int index = 0, slot = 0, size = 0;
        while (index < nums.size())
        {
            if (nums[index] != val)
            {
                nums[slot++] = nums[index];
                size++;
            }
            index++;
        }
        return size;
    }
};