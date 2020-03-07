class Solution
{
public:
    int climbStairs(int n)
    {
        unordered_map<int, int> cache{{1, 1}, {2, 2}};
        return recursive(n, cache);
    }

    int recursive(int n, unordered_map<int, int> &cache)
    {

        if (cache.find(n) == cache.end())
        {
            cache[n] = recursive(n - 1, cache) + recursive(n - 2, cache);
        }
        return cache[n];
    }
};