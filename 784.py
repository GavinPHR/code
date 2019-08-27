# Letter Case Permutation
from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        letters = set((x for x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        ans = [""]
        for c in S:
            tmp = []
            while ans:
                t = ans.pop()
                if c in letters:
                    tmp.append(t + c.lower())
                    tmp.append(t + c.upper())
                else:
                    tmp.append(t + c)
            ans = tmp
        return ans
s = Solution()
print(s.letterCasePermutation("a1b2"))