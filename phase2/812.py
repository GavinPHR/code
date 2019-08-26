# Largest Triangle Area
from typing import List
import math

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        l = len(points)
        ans = 0
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                p1, p2 = points[i], points[j]
                v_b = [p2[1] - p1[1], p2[0] - p1[0]]
                m_b = math.sqrt(v_b[0] ** 2 + v_b[1] ** 2)
                vnp_b = [-v_b[1] / m_b, v_b[0] / m_b]
                for k in range(j + 1, l):
                    p3 = points[k]
                    v_d = [p3[1] - p2[1], p3[0] - p2[0]]
                    m_h = abs(vnp_b[0] * v_d[0] + vnp_b[1] * v_d[1])
                    ans = max(ans, m_b * m_h)
        return ans / 2

s = Solution()
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print(s.largestTriangleArea(points))