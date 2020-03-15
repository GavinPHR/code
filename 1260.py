# Shift 2D Grid
from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                idx = (i*n+j+k) % (m*n)
                ans[idx//n][idx%n] = num
        return ans
            