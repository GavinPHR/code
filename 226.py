# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def bfs(node):
            if not node: return
            tmp = node.left
            node.left = node.right
            node.right = tmp
        q = collections.deque([root])
        while q:
            node = q.popleft()
            bfs(node)
            if node:
                q.append(node.left)
                q.append(node.right)
        return root
        