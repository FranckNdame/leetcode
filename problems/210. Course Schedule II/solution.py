from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adj_list = defaultdict(list)
        inDegrees = [0]*numCourses
        
        for u,v in prerequisites:
            adj_list[v].append(u)
            inDegrees[u] += 1
        
        queue = deque()
        self.enqueue(inDegrees, queue)
        
        while queue:
            currVertex = queue.popleft()
            order.append(currVertex)
            numCourses -= 1
            
            for neighbour in adj_list[currVertex]:
                inDegrees[neighbour] -= 1
            self.enqueue(inDegrees, queue)
        
        if numCourses: return []
        return order
    
    def enqueue(self, degrees, queue):
        for index, degree in enumerate(degrees):
            if not degree:
                queue.append(index)
                degrees[index] -= 1
        