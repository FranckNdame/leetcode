class Solution
{
public:
    int minPathSum(vector<vector<int>> &grid)
    {
        int N(grid.size());
        int M(grid[0].size());
        vector<vector<int>> dp(N, vector<int>(M, 0));
        for (int row = 0; row < N; row++)
        {
            for (int col = 0; col < M; col++)
            {
                if (col == 0 && row == 0)
                    dp[row][col] = grid[row][col];
                else
                    dp[row][col] = grid[row][col] + min(row == 0 ? INT_MAX : dp[row - 1][col], col == 0 ? INT_MAX : dp[row][col - 1]);
            }
        }
        return dp[N - 1][M - 1];
    }
};