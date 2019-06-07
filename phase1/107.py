# Binary Tree Level Order Traversal II
from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = collections.deque()
        q = collections.deque()
        q.append(root)
        count = len(q)
        while count:
            ans.appendleft([x.val for x in q])
            for i in range(count):
                x = q.popleft()
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            count = len(q)
        return list(ans)

if __name__ == '__main__':
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)
    s = Solution()
    print(s.levelOrderBottom(t))

