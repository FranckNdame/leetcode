class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) <= 1:
            return True
        A, B = {}, {}
        visits = {}
        self.result = True

        def dfs(vertex, A, B, graph):
            if vertex in B:
                self.result = False
            A[vertex] = True
            visits[vertex] = True
            for u in graph[vertex]:
                if u not in B:
                    dfs(u, B, A, graph)

        for node in range(len(graph)):
            if node not in visits:
                dfs(node, A, B, graph)

        return self.result
