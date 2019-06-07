# Binary Tree Inorder Traversal
# Iterative with a implemented stack (instead of call stack)
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans.append(node.val)
            node = node.right
        return ans


if __name__ == '__main__':
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(3)
    s = Solution()
    print(s.inorderTraversal(t))
