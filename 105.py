# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        d = dict((n, i) for i, n in enumerate(inorder))
        def helper(start, end, preorder):
            nonlocal d, inorder
            if end <= start: return None
            n = preorder[0]
            root = TreeNode(n)
            root.left = helper(start, d[n], preorder[1:1+d[n]-start])
            root.right = helper(d[n]+1, end, preorder[1+d[n]-start:])
            return root
        return helper(0, len(preorder), preorder)
                            

            
            