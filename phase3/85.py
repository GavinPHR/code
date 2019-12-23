# Maximal Rectangle
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        N, M = len(matrix), len(matrix[0])
        for i in range(N):
            count = 0
            for j in range(M):
                if matrix[i][j] == '0':
                    count = 0
                    matrix[i][j] = count
                else:
                    count += 1
                    matrix[i][j] = count
        ans = 0
        for i in range(N):
            for j in range(M):
                k = i
                height = 1
                length = float('inf')
                while k >= 0 and matrix[k][j] != 0:
                    length = min(length, matrix[k][j])
                    ans = max(ans, length * height)
                    height += 1
                    k -= 1
        return ans
s = Solution()
m = [["0","1","1","0","1"],
     ["1","1","0","1","0"],
     ["0","1","1","1","0"],
     ["1","1","1","1","0"],
     ["1","1","1","1","1"],
     ["0","0","0","0","0"]]
print(s.maximalRectangle(m))