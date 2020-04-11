# Binary Tree Zigzag Level Order Traversal
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans = [[root.val]]
        forward = [root]
        reverse = []
        while forward or reverse:
            local_ans = []
            if forward:
                while forward:
                    cur = forward.pop()
                    if cur.right:
                        local_ans.append(cur.right.val)
                        reverse.append(cur.right)
                    if cur.left:
                        local_ans.append(cur.left.val)
                        reverse.append(cur.left)
            else:
                while reverse:
                    cur = reverse.pop()
                    if cur.left:
                        local_ans.append(cur.left.val)
                        forward.append(cur.left)
                    if cur.right:
                        local_ans.append(cur.right.val)
                        forward.append(cur.right)
            if local_ans:
                ans.append(local_ans)
        return ans
