"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        d = dict()
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur.val not in d:
                d[cur.val] = Node(cur.val)
            for nei in cur.neighbors:
                if nei.val not in d:
                    stack.append(nei)
                    d[nei.val] = Node(nei.val)
                d[cur.val].neighbors.append(d[nei.val])
        return d[node.val]