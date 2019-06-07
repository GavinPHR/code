# Valid Square
from typing import List
import math

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
            return False
        l = []
        l.append((p2[1] - p1[1], p2[0] - p1[0]))
        l.append((p3[1] - p1[1], p3[0] - p1[0]))
        l.append((p4[1] - p1[1], p4[0] - p1[0]))
        right = False
        for i in range(3):
            for j in range(i + 1, 3):
                if l[i][0] * l[j][0] == -l[i][1] * l[j][1]:
                    right = (i, j)
        if not right:
            return False
        ps = (p2, p3, p4)
        unknown = 3 - right[0] - right[1]
        eqSqDist = False
        for i in right:
            if not eqSqDist:
                eqSqDist = l[i][0] ** 2 + l[i][1] ** 2
                continue
            if eqSqDist != l[i][0] ** 2 + l[i][1] ** 2:
                eqSqDist = False
        if not eqSqDist:
            return False
        print(l)
        u = (l[right[0]][0] + l[right[1]][0], l[right[0]][1] + l[right[1]][1])
        u_dist = math.sqrt(u[0] ** 2 + u[1] ** 2)
        u_norm = (u[0] / u_dist, u[1] / u_dist)
        print(u_norm)
        x_co = p1[0] + u_norm[1] * math.sqrt(2 * eqSqDist)
        y_co = p1[1] + u_norm[0] * math.sqrt(2 * eqSqDist)
        print(x_co, y_co)
        if x_co < ps[unknown][0] + 0.01 and x_co > ps[unknown][0] - 0.01 and y_co < ps[unknown][1] + 0.01 and y_co > ps[unknown][1] - 0.01:
            return True
        return False


if __name__ == '__main__':
    p1 = [0,0]
    p2 = [1,1]
    p3 = [1,0]
    p4 = [0,1]
    s = Solution()
    print(s.validSquare([1,1],[0,1],[1,2],[0,0]))