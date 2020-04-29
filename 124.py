# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = -float('inf')
        def rec(root):
            nonlocal ans
            if not root: return 0
            left = max(0, rec(root.left))
            right = max(0, rec(root.right))
            ans = max(ans, left+right+root.val)
            return max(left+root.val, right+root.val)
        rec(root)
        return ans
            