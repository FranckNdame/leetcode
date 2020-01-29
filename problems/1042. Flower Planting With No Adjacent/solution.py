import collections
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        flowers = set([i+1 for i in range(5)])
        network = collections.defaultdict(list)
        gardens = [0]*N
        
        for path in paths:
            network[path[0]].append(path[1])
            network[path[1]].append(path[0])
        for index, garden in enumerate(gardens):
            neighbor_flowers = set()
            for neighbor in network[index+1]:
                neighbor_flowers.add(gardens[neighbor-1])
            flower = list(flowers - neighbor_flowers)[0]
            gardens[index] = flower
            
        return gardens