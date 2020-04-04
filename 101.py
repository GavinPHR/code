# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        s = [(root.left, root.right)]
        while s:
            l, r = s.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            s.append((l.right, r.left))
            s.append((l.left, r.right))
        return True