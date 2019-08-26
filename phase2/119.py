# Pascal's Triangle II
from typing import List
import math

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [0] * (rowIndex + 1)
        m = math.ceil((rowIndex + 1) / 2)
        for i in range(m):
            ans[i] = math.factorial(rowIndex) // (math.factorial(rowIndex - i) * math.factorial(i))
        for i in range(-1, -m - 1, -1):
            ans[i] = ans[abs(i) - 1]
        return ans

s = Solution()
print(s.getRow(1))
