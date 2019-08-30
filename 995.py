# Minimum Number of K Consecutive Bit Flips
from typing import List
import collections

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        ans = 0
        q = collections.deque()
        for i, n in enumerate(A):
            if q:
                while q and i - q[0] >= K: q.popleft()
            if (n == 0 and len(q) % 2 == 0) or (n == 1 and len(q) % 2 == 1):
                if len(A) - i < K: return -1
                q.append(i)
                ans += 1
            else: continue
        return ans

s = Solution()
print(s.minKBitFlips([0,0,0,1,0,1,1,0], 3))