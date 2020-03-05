class Solution
{
public:
    std::vector<int> intersection(std::vector<int> &num1, std::vector<int> &num2)
    {
        std::vector<int> result;
        std::unordered_map<int, int> lookup;
        for (int num : num1)
            lookup.insert({num, 1});

        for (int num : num2)
        {
            if (lookup[num] == 0)
                continue;
            lookup[num]--;
            result.push_back(num);
        }

        return result;
    }
};