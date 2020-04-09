class Solution
{

public:
    // Approach One (Top-Down)
    int longestPalindromeSubseq(string s)
    {
        unordered_map<string, int> cache;
        return longestPalindromeSubseq(s, 0, s.size() - 1, cache);
    }

    int longestPalindromeSubseq(string &s, int start, int end, unordered_map<string, int> &cache)
    {
        if (start == end)
            return 1;
        if (start > end)
            return 0;
        string key = to_string(start) + "." + to_string(end);
        if (cache.find(key) == cache.end())
        {
            if (s[start] == s[end])
            {
                cache[key] = 2 + longestPalindromeSubseq(s, start + 1, end - 1, cache);
            }
            else
            {
                cache[key] = max(longestPalindromeSubseq(s, start + 1, end, cache), longestPalindromeSubseq(s, start, end - 1, cache));
            }
        }
        return cache[key];
    }

    // Approach Two (Bottom-Up)
    int longestPalindromeSubseq(string s)
    {
        int N = s.size();
        if (N < 2)
            return N;
        vector<vector<int>> grid(N, vector<int>(N, 0));
        for (int i = 0; i < N; i++)
            grid[i][i] = 1;
        for (int i = 1; i < N; i++)
        {
            for (int j = 0; j + i < N; j++)
            {
                if (s[j] == s[j + i])
                {
                    grid[j][j + i] = grid[j + 1][j + i - 1] + 2;
                }
                else
                {
                    grid[j][j + i] = max(grid[j + 1][j + i], grid[j][j + i - 1]);
                }
            }
        }

        return grid[0][N - 1];
    }
};
