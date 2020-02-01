class Solution:
    def findItinerary(self, tickets):
        adj_list = collections.defaultdict(list)

        for fr, to in sorted(tickets)[::-1]:
            adj_list[fr].append(to)

        route, stack = [], ['JFK']

        while stack:
            while adj_list[stack[-1]]:
                stack.append(adj_list[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]
