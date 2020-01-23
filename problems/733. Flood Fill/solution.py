class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        
        def dfs(row, col):
            if image[row][col] == color:
                image[row][col] = newColor
                if row > 0: dfs(row - 1, col)
                if row < R - 1: dfs(row + 1, col)
                if col > 0: dfs(row, col - 1)
                if col < C - 1: dfs(row, col + 1)
        
        dfs(sr,sc)
        return image
        