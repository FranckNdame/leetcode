"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        # store copy of node
        hashmap = {node : Node(node.val)}
        queue = deque([node])
        
        while queue:
            currNode = queue.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in hashmap:
                    hashmap[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                hashmap[currNode].neighbors.append(hashmap[neighbor])
        
        return hashmap[node]
        
        
        