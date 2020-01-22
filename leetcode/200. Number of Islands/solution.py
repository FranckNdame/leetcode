class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visits = {}
        islands = 0

        for row_i in range(len(grid)):
            for col_i in range(len(grid[0])):
                point = (row_i, col_i)
                if point not in visits and grid[point[0]][point[1]] == "1":
                    visits[point] = True
                    length = self.getLength(row_i, col_i, grid, visits)

                    if length > 0:
                        islands += 1

        return islands

    def getLength(self, row, col, grid, visits):
        length = 0
        stack = [(row, col)]

        while stack:
            length += 1
            curr = stack.pop()
            neighbours = self.getNeighbours(curr[0], curr[1], grid)
            for n in neighbours:
                if n not in visits and grid[n[0]][n[1]] == "1":
                    visits[n] = True
                    stack.append(n)
        return length

    def getNeighbours(self, row, col, grid):
        neighbours = []

        if row > 0:
            neighbours.append((row - 1, col))
        if row < len(grid) - 1:
            neighbours.append((row + 1, col))
        if col > 0:
            neighbours.append((row, col - 1))
        if col < len(grid[0]) - 1:
            neighbours.append((row, col + 1))
        return neighbours
