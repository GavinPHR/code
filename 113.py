# Path Sum II
from typing import List
from binarytree import TreeNode, makeTree, inOrder


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        def dfs(node, currentsum, path, sum):
            if not node.left and not node.right:
                if currentsum + node.val == sum:
                    ans.append(list(path) + [node.val])
            currentsum += node.val
            path.append(node.val)
            if node.left:
                dfs(node.left, currentsum, list(path), sum)
            if node.right:
                dfs(node.right, currentsum, list(path), sum)
        dfs(root, 0, [], sum)
        return ans

if __name__ == '__main__':
    t = makeTree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    t1 = makeTree([-2,None,-3])
    s = Solution()
    print(s.pathSum(t1, -5))