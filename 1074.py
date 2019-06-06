# Number of Submatrices That Sum to Target
from typing import List
import collections

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def findTarget(arr):
            ret = 0
            s = 0
            c = collections.Counter({0:1})
            for n in arr:
                s += n
                if c[s - target]:
                    ret += c[s - target]
                c[s] += 1
            return ret
        n, m, ans = len(matrix), len(matrix[0]), 0
        for i in range(n):
            arr = [0] * m
            for j in range(i, n):
                for k, ns in enumerate(matrix[j]):
                    arr[k] += ns
                ans += findTarget(arr)
        return ans

if __name__ == '__main__':
    m = [[0,1,0],[1,1,1],[0,1,0]]
    s = Solution()
    print(s.numSubmatrixSumTarget(m, 0))