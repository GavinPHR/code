# Minimum Falling Path Sum
from typing import List


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        for i in range(1, n):
            A[i][0] = min(A[i - 1][0] + A[i][0],
                          A[i - 1][1] + A[i][0])
            for j in range(1, n - 1):
                A[i][j] = min(A[i - 1][j - 1] + A[i][j],
                              A[i - 1][j]     + A[i][j],
                              A[i - 1][j + 1] + A[i][j])
            A[i][n - 1] = min(A[i - 1][n - 1] + A[i][n - 1],
                              A[i - 1][n - 2] + A[i][n - 1])
        return min(A[-1])


# Use indexing instead of the mess
