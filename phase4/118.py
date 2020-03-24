# Pascal's Triangle
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        ans = [[1]]
        if numRows == 1: return ans
        for n in range(2, numRows + 1):
            tmp = [0] * n
            tmp[0], tmp[-1] = 1, 1
            for i in range(1, n):
                tmp[i] = ans[-1][i] + ans[-1][i-1]
            ans.append(tmp)
        return ans