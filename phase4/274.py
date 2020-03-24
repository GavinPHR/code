# H-Index
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1
        acc = 0
        print(buckets)
        for i in range(n, -1, -1):
            acc += buckets[i]
            if acc >= i:
                return i
        return 0

s = Solution()
# print(s.hIndex([3,0,6,1,5]))
print(s.hIndex([]))