# Max Increase to Keep City Skyline
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        N = len(grid)
        rows, cols = [None] * N, [None] * N
        for i in range(N):
            max_row, max_col = 0, 0
            for j in range(N):
                if grid[i][j] > max_row:
                    max_row = grid[i][j]
                if grid[j][i] > max_col:
                    max_col = grid[j][i]
            rows[i] = max_row
            cols[i] = max_col
        ans = 0
        for i in range(N):
            for j in range(N):
                ans += min(rows[i], cols[j]) - grid[i][j]
        return ans
# class Solution:
#     def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
#         row_max = [max(row) for row in grid]
#         col_max = [max(col) for col in zip(*grid)]
#
#         return sum(min(row_max[r], col_max[c]) - val
#                    for r, row in enumerate(grid)
#                    for c, val in enumerate(row))


if __name__ == '__main__':
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    s = Solution()
    print(s.maxIncreaseKeepingSkyline(grid))