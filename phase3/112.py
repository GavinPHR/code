# Path Sum
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        stack = [root]
        while stack:
            n = stack.pop()
            l = n.left
            r = n.right
            if not l and not r and n.val == sum: return True
            if l:
                l.val += n.val
                stack.append(l)
            if r:
                r.val += n.val
                stack.append(r)
        return False