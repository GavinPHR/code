# Reshape the Matrix
from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(nums), len(nums[0])
        if n * m != r * c: return nums
        ans = [[0] * c for _ in range(r)]
        ii, jj = 0, 0
        for i in range(r):
            for j in range(c):
                ans[i][j] = nums[ii][jj]
                jj += 1
                if jj == m:
                    ii += 1
                    jj = 0
        return ans



s = Solution()
print(s.matrixReshape([[1,2],
 [3,4]], 1, 4))