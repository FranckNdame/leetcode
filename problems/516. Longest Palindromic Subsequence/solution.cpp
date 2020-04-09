class Solution
{

public:
    // Approach One (Top-Down)
    int longestPalindromeSubseq(string s)
    {
        int n = s.size();
        vector<vector<int>> mem(n, vector<int>(n));
        return longestPalindromeSubseq(0, n - 1, s, mem);
    }
    int longestPalindromeSubseq(int l, int r, string &s, vector<vector<int>> &mem)
    {
        if (l == r)
            return 1;
        if (l > r)
            return 0;
        if (mem[l][r])
            return mem[l][r];
        return mem[l][r] = s[l] == s[r] ? 2 + longestPalindromeSubseq(l + 1, r - 1, s, mem) : max(longestPalindromeSubseq(l + 1, r, s, mem), longestPalindromeSubseq(l, r - 1, s, mem));
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

    // Approach 3
    int longestPalindromeSubseq(string s)
    {
        int n = s.size();
        vector<int> v0(n), v1(n, 1), v(n), *i_2 = &v0, *i_1 = &v1, *i_ = &v;
        for (int i = 2; i <= n; i++)
        {                                       //length
            for (int j = 0; j < n - i + 1; j++) //start index
                i_->at(j) = s[j] == s[i + j - 1] ? 2 + i_2->at(j + 1) : max(i_1->at(j), i_1->at(j + 1));
            swap(i_1, i_2);
            swap(i_1, i_); //rotate i_2, i_1, i_
        }
        return i_1->at(0);
    }
};
