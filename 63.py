# Unique Paths II
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            obstacleGrid[i][0] = -1
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                break
            obstacleGrid[0][i] = -1
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    continue
                l = obstacleGrid[i][j - 1] if obstacleGrid[i][j - 1] != 1 else 0
                r = obstacleGrid[i - 1][j] if obstacleGrid[i - 1][j] != 1 else 0
                obstacleGrid[i][j] = l + r
        return abs(obstacleGrid[-1][-1])


if __name__ == '__main__':
    g = [
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]
    s = Solution()
    print(s.uniquePathsWithObstacles(g))
    print(g)