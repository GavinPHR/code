# Unique Binary Search Trees II
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        prev = [TreeNode(1)]
        def copyTree(node):
            newnode = TreeNode(node.val)
            if node.left != None:
                newnode.left = copyTree(node.left)
            if node.right != None:
                newnode.right = copyTree(node.right)
            return newnode
        for i in range(2, n+1):
            now = []
            for p in prev:
                t = TreeNode(i)
                t.left = p
                now.append(copyTree(t))
                cur = p
                while cur.right:
                    tmp = cur.right
                    cur.right = TreeNode(i)
                    cur.right.left = tmp
                    now.append(copyTree(p))
                    cur.right = cur.right.left
                    cur = cur.right
                cur.right = TreeNode(i)
                now.append(p)
            prev = now
        return prev


s = Solution()
print(s.generateTrees(3))