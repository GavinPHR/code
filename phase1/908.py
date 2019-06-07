# Smallest Range I
from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        r, l = max(A) - K, min(A) + K
        if r <= l:
            return 0
        else:
            return r - l

if __name__ == '__main__':
    A = [1, 3, 6]
    K = 3
    s = Solution()
    print(s.smallestRangeI([0,10], 2))