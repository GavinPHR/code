# Shortest Subarray with Sum at Least K
from typing import List
import collections

class Solution:
    def shortestSubarray(self, A, K):
        N = len(A)
        B = [0] * (N + 1)
        for i in range(N): B[i + 1] = B[i] + A[i]
        d = collections.deque()
        res = N + 1
        for i in range(N + 1):
            while d and B[i] - B[d[0]] >= K: res = min(res, i - d.popleft())
            while d and B[i] <= B[d[-1]]: d.pop()
            d.append(i)
        return res if res <= N else -1


s = Solution()
a= [-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6]
print(s.shortestSubarray(a,151))