# Maximum Depth of N-ary Tree


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if root.children == []:
            return 1
        return 1 + max(self.maxDepth(x) for x in root.children)
"""
if __name__ == '__main__':
    t = Node(1, [Node(3),Node(2),Node(4)])
    t.children[0].children = []
""
