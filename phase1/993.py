# Cousins in Binary Tree
from binarytree import TreeNode, makeTree
import collections

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        def re(root, val, level):
            if not root:
                return
            if root.left and root.left.val == val:
                return (level + 1, root.val)
            if root.right and root.right.val == val:
                return (level + 1, root.val)
            l = re(root.left, val, level + 1)
            r = re(root.right, val, level + 1)
            return l if l else r
        a = re(root, x, 0)
        b = re(root, y, 0)
        if a[0] != b[0]:
            return False
        if a[1] == b[1]:
            return False
        return True


if __name__ == '__main__':
    root = makeTree([1,2,3,None,4,None,5])
    s = Solution()
    print(s.isCousins(root, 4, 5))