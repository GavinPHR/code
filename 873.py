# Length of Longest Fibonacci Subsequence
from typing import List
import collections

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        idx = {n:i for i, n in enumerate(A)}
        pairs = collections.Counter()
        ans = 2
        for i in range(n - 1):
            for j in range(i + 1, n):
                num = A[j] - A[i]
                if num in idx and idx[num] < i:
                    pairs[(i, j)] = pairs[(idx[num], i)] + 1
                    ans = max(pairs[(i,j)] + 2, ans)
        print(pairs)
        return ans if ans != 2 else 0



s = Solution()
a = [1,2,3,4,5,6,7,8]
b = [2,4,5,6,7,8,11,13,14,15,21,22,34]
print(s.lenLongestFibSubseq(b))