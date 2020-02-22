class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visits = {}
        perimeter = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    visits[(row, col)] = True
                    stack = [(row, col)]
                    while stack:
                        cRow, cCol = stack.pop()
                        potentialNeighbours = [
                            (cRow+1, cCol), (cRow-1, cCol), (cRow, cCol+1), (cRow, cCol-1)]
                        neighbours = [(r, c) for r, c in potentialNeighbours if 0 <= r < len(
                            grid) and 0 <= c < len(grid[0]) and grid[r][c]]
                        perimeter += (len(potentialNeighbours) -
                                      len(neighbours))
                        for nr, nc in neighbours:
                            if (nr, nc) not in visits:
                                visits[(nr, nc)] = True
                                stack.append((nr, nc))
                    return perimeter
