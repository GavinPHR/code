# Maximal Square
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        pts =set((i,j) for i in range(n) for j in range(m) if matrix[i][j] == "1" )
        if not pts: return 0
        s = 0
        while pts:
            print(pts)
            ss = s + 1
            rm = set()
            for p in pts:
                _i, _j = p[0] + ss, p[1] + ss
                if _i >= n or _j >= m or matrix[_i][_j] != "1":
                    rm.add(p)
                    continue
                flag = True
                for i in range(p[0], _i):
                    if matrix[i][_j] != "1":
                        flag = False
                        break
                if flag:
                    for j in range(p[1], _j):
                        if matrix[_i][j] != "1":
                            flag = False
                            break
                if not flag:
                    rm.add(p)
            pts.difference_update(rm)
            rm = set()
            if pts:
                s += 1
        return (s + 1) * (s + 1)



s = Solution()
m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","1","1","1"]]
for row in m:
    print(row)
print(s.maximalSquare(m))