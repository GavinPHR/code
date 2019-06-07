# Squares of a Sorted Array
from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] = A[i] * A[i]
        A.sort()
        return A

if __name__ == '__main__':
    A = [-7, -3, 2, 3, 11]
    s = Solution()
    print(s.sortedSquares(A))