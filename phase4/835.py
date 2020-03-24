# Image Overlap
from typing import List
from collections import Counter

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        a, b, n = set(), set(), len(A)
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1: a.add((i, j))
                if B[i][j] == 1: b.add((i, j))
        c = Counter()

        for i, j in a:
            for ii, jj in b:
                c[complex(i-ii,j-jj)] += 1
        return max(c.values()) if c.values() else 0

s = Solution()
A = [[0]]
B = [[0]]
print(s.largestOverlap(A, B))