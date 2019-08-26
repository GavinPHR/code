# Set Matrix Zeroes
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zz = (not all(matrix[i][0] for i in range(len(matrix))), not all(matrix[0][j] for j in range(len(matrix[0]))))
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if n == 0:
                    matrix[i][0] = matrix[0][j] = None
        for i in range(1, len(matrix)):
            if not matrix[i][0]:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        for j in range(1, len(matrix[0])):
            if not matrix[0][j]:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        if zz[0]:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if zz[1]:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        return

s = Solution()
a = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
b= [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
s.setZeroes(a)
print(a)
