# Range Sum of BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inOrder(self, node, L, R, sum):
        if not node: return
        if node.val < L:
            self.inOrder(node.right, L, R, sum)
        elif node.val > R:
            self.inOrder(node.left, L, R, sum)
        else:
            sum[0] += node.val
            self.inOrder(node.right, L, R, sum)
            self.inOrder(node.left, L, R, sum)


    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        sum = [0]
        self.inOrder(root, L, R, sum)
        return sum[0]


