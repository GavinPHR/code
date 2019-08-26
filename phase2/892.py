# Surface Area of 3D Shapes
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans = 0
        l = len(grid)
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 0: continue
                ans += 2
                for x ,y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if x < 0 or x >= l or y < 0 or y >= l:
                        ans += n
                    else:
                        ans += max(n - grid[x][y], 0)
        return ans

s = Solution()
print(s.surfaceArea([[1,2],[3,4]]))