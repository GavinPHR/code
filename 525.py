# Contiguous Array
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = dict()
        o, z, ans = 0, 0, 0
        d[0] = -1
        for i, n in enumerate(nums):
            if n == 1: o += 1
            else: z += 1
            k = o - z
            if d.get(k, -2) >= -1:
                ans = max(ans, i - d[k])
            else:
                d[k] = i
        print(d)
        return ans


s = Solution()
print(s.findMaxLength([0,0,1]

))
