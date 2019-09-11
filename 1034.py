# Coloring A Border
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        init = grid[r0][c0]
        n, m = len(grid), len(grid[0])
        seen = set()
        boarder = set()
        stack = [(r0, c0)]
        while stack:
            i, j = stack.pop()
            if (i, j) in seen: continue
            for ii, jj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if ii < 0 or jj <0 or ii >= n or jj >= m:
                    boarder.add((i, j))
                    continue
                if grid[ii][jj] != init:
                    boarder.add((i,j))
                else:
                    stack.append((ii, jj))
            seen.add((i,j))
        for i, j in boarder: grid[i][j] = color
        return grid




s = Solution()
grid = [[1,1,1],[1,1,1],[1,1,1]]
r0 = 1
c0 = 1
color = 2
print(s.colorBorder(grid, r0, c0, color))
