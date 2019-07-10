# Number of Islands
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        n, m, ans = len(grid), len(grid[0]), 0
        for i in range(n):
            for j in range(m):
                tmp = grid[i][j]
                if tmp == "-1" or tmp == "0": continue
                ans += 1
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for p, q in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                        if p >= n or p < 0 or q >= m or q < 0: continue
                        if grid[p][q] == "1":
                            stack.append((p, q))
                            grid[p][q] = "-1"
        return ans


s = Solution()
print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))