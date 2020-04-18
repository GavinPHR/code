from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                candidate = float('inf')
                for di, dj in (-1, 0), (0, -1):
                    if i + di < 0 or j + dj < 0:
                        continue
                    candidate = min(candidate, grid[i + di][j + dj] + grid[i][j])
                grid[i][j] = candidate
        return grid[-1][-1]

s = Solution()
print(s.minPathSum([[1,2],[5,6],[1,1]]))