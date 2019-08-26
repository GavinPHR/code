# Range Addition II
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minx, miny = m, n
        for a, b in ops:
            minx, miny = min(a, minx), min(b, miny)
        return minx * miny

s = Solution()
print(s.maxCount(3, 3, [[2,2],[3,3]]))