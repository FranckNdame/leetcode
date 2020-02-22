class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = {}
        maxArea = -float('inf')
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == 1:
                    visited[(row, col)] = True
                    maxArea = max(maxArea, self.dfs(row, col, grid, visited))

        return 0 if maxArea == -float('inf') else maxArea

    def dfs(self, r, c, grid, visited) -> int:
        stack = [(r, c)]
        area = 0

        while stack:
            row, col = stack.pop()
            area += 1
            neighbours = [(row+1, col), (row-1, col),
                          (row, col+1), (row, col-1)]
            for nr, nc in neighbours:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] and (nr, nc) not in visited:
                    visited[(nr, nc)] = True
                    stack.append((nr, nc))
        return area
