# DI String Match
from typing import List

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        perm = [x for x in range(len(S)+1)]
        ans = []
        for c in S:
            if c == "I":
                ans.append(perm[0])
                del perm[0]
            else:
                ans.append(perm.pop())
        ans.append(perm[0])
        return ans
if __name__ == '__main__':
    a = "III"
    s = Solution()
    print(s.diStringMatch(a))