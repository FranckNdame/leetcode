class Solution:
    def maximumMinimumPath(self, A: [[int]]) -> int:
        visited = {}
        self.dfs((0, 0), A, {}, float('inf'), [])

    def dfs(self, point, grid, visited, minVal, path):
        row, col = point
        currVal = grid[row][col]
        # print(point, currVal)
        minVal = min(minVal, currVal)
        visited[point] = True
        path.append(currVal)

        # print(f"Value: {currVal} || Point: {point} || V: {visited} || m: {minVal}")
        if point == (len(grid)-1, len(grid[0])-1):
            print(f"Goal reached ==> minVal: {minVal} \npath: {path} \n\n")
        n = []
        for nr, nc in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                n.append((nr, nc))

        for nr, nc in list(reversed(sorted(n, key=lambda x: grid[x[0]][x[1]]))):
            visited[(nr, nc)] = True
            self.dfs((nr, nc), grid, visited.copy(), minVal, path[:])
            # n.append((nr, nc))


grid = [
    [5, 4, 5],
    [1, 2, 6],
    [7, 4, 6]
]
solution = Solution()
solution.maximumMinimumPath(
    [[2, 0, 5, 2, 0],
     [2, 4, 4, 4, 3],
     [1, 5, 0, 0, 0],
     [5, 4, 4, 3, 1],
     [1, 3, 1, 5, 3]])
