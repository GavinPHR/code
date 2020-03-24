# Maximum Product of Splitted Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxProduct(self, root: TreeNode) -> int:

        def acc(node):
            if not node: return
            sum_ = node.val
            if node.left:
                acc(node.left)
                sum_ += node.left.val
            if node.right:
                acc(node.right)
                sum_ += node.right.val
            node.val = sum_

        acc(root)

        max_ = 0

        def cut(node, carry):
            nonlocal max_
            max_ = max(node.val * carry, max_)
            if node.left:
                cut(node.left, carry + node.val - node.left.val)
            if node.right:
                cut(node.right, carry + node.val - node.right.val)

        cut(root, 0)

        return max_ % (10**9+7)