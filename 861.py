# Score After Flipping Matrix
from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[i])):
                    A[i][j] = 0 if A[i][j] else 1
        print(A)
        base2 = []
        for i in range(len(A[0]) - 1, 0, -1):
            zeros, ones = 0, 0
            for j in range(len(A)):
                if A[j][i] == 1:
                    ones += 1
                else:
                    zeros += 1
            base2.append(max(zeros, ones))
        ans = 0
        exp = 1
        for i in base2:
            ans += i * exp
            exp *= 2
        return ans + len(A) * exp




if __name__ == '__main__':
    s = Solution()
    print(s.matrixScore([[0],[0],[0]]))
    #39