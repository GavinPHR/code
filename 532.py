# K-diff Pairs in an Array
from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0: return 0
        seen = set()
        pool = set()
        for n in nums:
            if n + k in seen:
                pool.add((n,n+k))
            if n - k in seen:
                pool.add((n-k,n))
            seen.add(n)
        print(pool)
        return len(pool)


s = Solution()
print(s.findPairs([1,1,1,2,1],1))