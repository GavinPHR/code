# Array of Doubled Pairs
from typing import List
import collections

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        c = collections.Counter(A)
        for i in sorted(c, key = abs):
            if c[i] > c[2*i]:
                return False
            else:
                c[2*i] -= c[i]
        return True

s = Solution()
print(s.canReorderDoubled([2,4,-2,-4]))