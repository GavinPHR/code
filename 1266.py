# Minimum Time Visiting All Points
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x, y = points.pop()
        ans = 0
        while points:
            a, b = points.pop()
            ans += max(abs(x-a), abs(y-b))
            x, y = a, b
        return ans