# Island Perimeter
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m, ans = len(grid), len(grid[0]), 0
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n:
                    ans += 4
                    if i - 1 >= 0 and grid[i - 1][j]: ans -= 2
                    if j - 1 >= 0 and grid[i][j - 1]: ans -= 2
        return ans

s = Solution()
print(s.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))