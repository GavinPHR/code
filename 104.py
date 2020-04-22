# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0
        if not root: return 0
        stack = [(root, 1)]
        while stack:
            cur, i = stack.pop()
            if cur is not None:
                stack.append((cur.left, i+1))
                stack.append((cur.right, i+1))
                ans = max(i, ans)
        return ans