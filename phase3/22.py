# Generate Parentheses
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = 2 * n
        ans = [[None] * l]
        while True:
            print(ans)
            mod = False
            new = []
            while ans:
                tmp = ans.pop()
                i = 0
                while i != l and tmp[i]: i += 1
                if i == l:
                    new.append(tmp)
                    continue
                mod = True
                tmp[i] = "("
                for j in range(i + 1, l, 2):
                    if not tmp[j]:
                        dup = tmp.copy()
                        dup[j] = ")"
                        new.append(dup)
            ans = new
            if mod == False:
                break
        return list(set(["".join(x) for x in ans]))
s = Solution()
print(s.generateParenthesis(3))