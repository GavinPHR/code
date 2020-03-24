# Diameter of Binary Tree
import binarytree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        ans = 0
        def re(n: TreeNode):
            nonlocal ans
            if not n.left and not n.right: return 0
            dl, dr = 0, 0
            if n.left:
                dl = re(n.left) + 1
            if n.right:
                dr = re(n.right) + 1
            ans = max(ans, dl+dr)
            return max(dl, dr)
        re(root)
        return ans

