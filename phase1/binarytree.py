from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def makeTree(vals: List[int]) -> TreeNode:
    q = deque()
    root = TreeNode(vals[0])
    q.append(root)
    for i in range(1, len(vals), 2):
        x = q.popleft()
        #print(vals[i])
        if vals[i]:
            x.left = TreeNode(vals[i])
            q.append(x.left)
        if vals[i + 1]:
            x.right = TreeNode(vals[i+1])
            q.append(x.right)
    return root

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

if __name__ == '__main__':
    x = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    inOrder(makeTree(x))