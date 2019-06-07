# Find Mode in Binary Search Tree
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder(self, node):
        if node is None:
            return
        if node.left is not None:
            for x in self.inorder(node.left) :
                yield x
        yield node
        if node.right is not None:
            for x in self.inorder(node.right) :
                yield x


    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        tups = []
        prev, count = root.val, 0
        for node in self.inorder(root):
            if node.val == prev:
                count += 1
            else:
                tups.append((count, prev))
                prev, count = node.val, 1
        tups.append((count, prev))
        tups.sort(reverse=True)
        print(tups)
        maxcount = tups[0][0]
        ans, i = [], 0
        while tups[i][0] == maxcount:
            ans.append(tups[i][1])
            if i == len(tups) - 1:
                break
            i += 1
        return ans

if __name__ == '__main__':
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(2)
    t2 = TreeNode(1)
    s = Solution()
    print(s.findMode(t2))
