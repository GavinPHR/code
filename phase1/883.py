# Projection Area of 3D Shapes
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        bottom = 0
        left_p, right_p = [-1] * len(grid), [-1] * len(grid)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    bottom += 1
                    right_p[j] = grid[i][j] if grid[i][j] > right_p[j] else right_p[j]
                    left_p[i] = grid[i][j] if grid[i][j] > left_p[i] else left_p[i]
        print(left_p)
        print(right_p)
        return bottom + sum(left_p) + sum(right_p)

if __name__ == '__main__':
    g = [[2,2,2],[2,1,2],[2,2,2]]
    g1 = [[1,2],[3,4]]
    s = Solution()
    print(s.projectionArea([[1,4],[1,1]]))