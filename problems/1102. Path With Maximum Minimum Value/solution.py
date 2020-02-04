class Solution:
    def maximumMinimumPath(self, matrix: List[List[int]]) -> int:
        target = (len(matrix)-1, len(matrix[0])-1)
        heap = [(-matrix[0][0], (0, 0))]
        visited = {(0, 0): True}

        while heap:
            node, coord = heapq.heappop(heap)
            if coord == target:
                return abs(node)
            r, c = coord
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and (nr, nc) not in visited:
                    visited[(nr, nc)] = True
                    nextNode = -matrix[nr][nc]
                    heapq.heappush(heap, (max(node, nextNode), (nr, nc)))
