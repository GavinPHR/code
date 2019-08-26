# Maximum Width Ramp
from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        if not A: return 0
        idx = [i for i in range(len(A))]
        idx.sort(key=lambda x: A[x])
        m = idx[0]
        ans = 0
        for i in idx:
            if i < m:
                m = i
                continue
            ans = max(ans, i - m)
        return ans

s = Solution()
print(s.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))