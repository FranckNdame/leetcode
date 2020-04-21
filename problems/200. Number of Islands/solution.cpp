class Solution
{
public:
    int numIslands(vector<vector<char>> &grid)
    {
        if (!grid.size())
            return 0;
        int N(grid.size()), M(grid[0].size());
        int islands(0);
        vector<vector<bool>> cache(N, vector<bool>(M, false));
        for (int row = 0; row < N; row++)
        {
            for (int col = 0; col < M; col++)
            {
                if (cache[row][col] || grid[row][col] == '0')
                    continue;
                dfs(grid, row, col, cache);
                islands++;
            }
        }

        return islands;
    }

    void dfs(vector<vector<char>> &grid, int row, int col, vector<vector<bool>> &cache)
    {
        int N(grid.size()), M(grid[0].size());
        stack<pair<int, int>> stack({make_pair(row, col)});
        cache[row][col] = true;
        while (!stack.empty())
        {
            int cr = stack.top().first;
            int cc = stack.top().second;
            stack.pop();
            vector<pair<int, int>> neighbours({{cr, cc + 1}, {cr, cc - 1}, {cr + 1, cc}, {cr - 1, cc}});
            for (auto neigh : neighbours)
            {
                int nr(neigh.first), nc(neigh.second);
                if (nr >= 0 && nr < N && nc >= 0 && nc < M && grid[nr][nc] == '1' && cache[nr][nc] == false)
                {
                    cache[nr][nc] = true;
                    stack.push(make_pair(nr, nc));
                }
            }
        }
    }
};