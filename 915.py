# Partition Array into Disjoint Intervals
from typing import List


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        p1, p2 = 0, 1
        maxN = A[0]
        while p2 < len(A):
            if A[p2] < maxN:
                maxN = max(maxN, max(A[p1+1:p2+1]))
                p1 = p2
            p2 += 1
        return p1 + 1

s = Solution()
print(s.partitionDisjoint([1,1,1,0,6,12]))
