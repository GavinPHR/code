# Partition Array Into Three Parts With Equal Sum
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        acc = 0
        d = dict()
        for i, n in enumerate(A):
            acc += n
            if d.get(acc): d[acc].append(i)
            else: d[acc] = [i]
        if acc % 3 != 0: return False
        target = acc // 3
        if not d.get(target): return False
        idx = d[target][0]
        target *= 2
        if not d.get(target): return False
        if idx >= d[target][-1] or  d[target][-1] == len(A) - 1: return False
        return True





s = Solution()
print(s.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
