class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int result = 0;
        int left = 0;
        int right = height.size() - 1;
        while (left < right)
        {
            int area = std::min(height[left], height[right]) * (right - left);
            result = std::max(result, area);
            if (height[left] < height[right])
                left++;
            else
                right--;
        }

        return result;
    }
};
