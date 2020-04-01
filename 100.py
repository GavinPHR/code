
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        s1 = [p]
        s2 = [q]
        while s1:
            a, b = s1.pop(), s2.pop()
            if not a or not b:
                if not a and not b:
                    continue
                else:
                    return False
            
            if a.val != b.val:
                return False
            s1.append(a.left)
            s2.append(b.left)
            s1.append(a.right)
            s2.append(b.right)

        return True