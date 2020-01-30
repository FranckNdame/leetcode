from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        neighbors = [[] for _ in range(numCourses)]
        degrees = [0]*numCourses
        queue = deque()

        for u, v in prerequisites:
            neighbors[v].append(u)
            degrees[u] += 1

        self.addToQueue(queue, degrees)
        while queue:
            currVertex = queue.popleft()
            numCourses -= 1
            for neighbor in neighbors[currVertex]:
                degrees[neighbor] -= 1
            self.addToQueue(queue, degrees)
        print(degrees, numCourses)
        return numCourses == 0

    def addToQueue(self, q, degs):
        for index, deg in enumerate(degs):
            if not deg:
                q.append(index)
                degs[index] = -1
