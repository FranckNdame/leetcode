from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) < n-1: return []
        if n == 1: return [0]
        adj = defaultdict(list)
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                vertex = adj[leaf].pop()
                adj[vertex].remove(leaf)
                if len(adj[vertex]) == 1:
                    new_leaves.append(vertex)
            leaves = new_leaves
        
        return leaves
        