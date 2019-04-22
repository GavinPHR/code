# Merge Two Binary Trees

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def printval(self):
        if self.left:
            self.left.printval()
        print(self.val)
        if self.right:
            self.right.printval()

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and t2:
            return t2
        elif not t2 and t1:
            return t1
        elif not t2 and not t1:
            return None
        else:
            ans = TreeNode(t1.val + t2.val)
            ans.left = self.mergeTrees(t1.left, t2.left)
            ans.right = self.mergeTrees(t1.right, t2.right)
            return ans

if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)
    s = Solution()
    s.mergeTrees(t1,t2).printval()

