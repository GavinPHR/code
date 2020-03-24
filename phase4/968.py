# Binary Tree Cameras

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans = 0
        covered = {None}
        def dfs(node, parent=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                nonlocal covered, ans
                if node.left not in covered or node.right not in covered or (node not in covered and parent is None):
                    ans += 1
                    covered.update({node.left, node.left, parent, node})
        dfs(root)
        return ans

