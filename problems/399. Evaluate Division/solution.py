class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj_list = collections.defaultdict(list)
        result = []
        
        def dfs(fr, to, adj_list, answer, visits):
            stack = [(fr,to, 1)]
            while stack:
                print(stack)
                fr, to, cost = stack.pop()
                if fr == to: return cost
                visits[fr] = True
                for neigh, val in adj_list[fr]:
                    if neigh not in visits:
                        stack.append((neigh, to, cost*val))
            return -1

        
        for i, equation in enumerate(equations):
            u,v = equation
            adj_list[u].append((v,values[i]))
            adj_list[v].append((u, 1/values[i]))
        

        for u,v in queries:
            if u not in adj_list or v not in adj_list: result.append(-1)
            elif u == v: result.append(1)
            else: 
                cost = dfs(u,v,adj_list,1,{})
                print(cost)
                result.append(cost if cost else -1)
            
        return result
            
        