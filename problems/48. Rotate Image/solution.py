class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        # Transpose
        for i in range(N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse
        for i in range(N):
            for j in range(N//2):
                matrix[i][j], matrix[i][N-1-j] = matrix[i][N-1-j], matrix[i][j]
