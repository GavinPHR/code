# Number of Boomerangs
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p in points:
            s = {}
            for q in points:
                a, b = p[0] - q[0], p[1] - q[1]
                d = a * a + b * b
                s[d] = 1 + s.get(d, 0)
            for k in s:
                    ans += s[k] * (s[k] - 1)
        return int (ans)

s = Solution()
print(s.numberOfBoomerangs([[0,0],[1,0],[2,0]]))