class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edgeCount, totalCost = 0, 0
        visits = {}
        adj_list = collections.defaultdict(list)
        heap = []
        self.construct_adj_list(adj_list, pipes, wells)
        self.addEdges(1, visits, heap, adj_list)

        while heap and edgeCount != n:
            cost, u, v = heapq.heappop(heap)
            if v in visits:
                continue
            totalCost += cost
            edgeCount += 1
            self.addEdges(v, visits, heap, adj_list)
        return totalCost

    def construct_adj_list(self, adj_list, pipes, wells):
        n = len(wells)
        for u, v, cost in pipes:
            adj_list[u].append((v, cost))
            adj_list[v].append((u, cost))

        for index, cost in enumerate(wells):
            adj_list[n+1].append((index+1, cost))
            adj_list[index+1].append((n+1, cost))

    def addEdges(self, node, visits, heap, adj_list):
        visits[node] = True
        for to, cost in adj_list[node]:
            if to in visits:
                continue
            heapq.heappush(heap, (cost, node, to))
