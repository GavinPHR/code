# Binary Tree Level Order Traversal
from typing import List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans = []
        q = collections.deque()
        q.append(root)
        p = collections.deque()
        while q or p:
            level = []
            flag = True
            while q:
                tmp = q.popleft()
                level.append(tmp.val)
                if tmp.left: p.append(tmp.left)
                if tmp.right: p.append(tmp.right)
                flag = False
            while p and flag:
                tmp = p.popleft()
                level.append(tmp.val)
                if tmp.left: q.append(tmp.left)
                if tmp.right: q.append(tmp.right)
            ans.append(level)
        return ans


if __name__ == '__main__':
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)
    s = Solution()
    print(s.levelOrder(t))