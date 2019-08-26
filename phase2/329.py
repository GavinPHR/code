# Longest Increasing Path in a Matrix
from typing import List
import collections

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        path = [[1 for _ in range(m)] for _ in range(n)]
        d = collections.defaultdict(list)
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                for a, b in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if a < 0 or b < 0 or a >= n or b >= m: continue
                    if matrix[a][b] > num:
                        d[(i, j)].append((a, b))
        for i in range(n):
            for j in range(m):
                stack = [(a, b, 2) for a, b in d.get((i, j), [])]
                while stack:
                    a, b, l = stack.pop()
                    if path[a][b] >= l: continue
                    path[a][b] = l
                    stack.extend([(x, y, l + 1) for x, y in d.get((a, b), [])])
        return max([max(row) for row in path])






n = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
print(n[(1+1j)])
# s = Solution()
# print(s.longestIncreasingPath(n))