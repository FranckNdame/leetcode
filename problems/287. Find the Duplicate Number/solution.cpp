class Solution
{
public:
    int findDuplicate(vector<int> &nums)
    {
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; i++)
        {
            if (nums[i] == nums[i + 1])
                return nums[i];
        }

        return -1;
    }


    int findDuplicate(vector<int>& nums) {
        // Floyd's Tortoise and Hare
        int tortoise(nums[0]), hare(nums[0]);
        while (true) {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
            if (tortoise == hare) break;
        }
        
        int ptr1(nums[0]), ptr2(hare);
        
        while (ptr1 != ptr2) {
            ptr1 = nums[ptr1];
            ptr2 = nums[ptr2];
        }
        
        return ptr1;
    }
};