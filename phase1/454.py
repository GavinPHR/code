# 4Sum II
from typing import List
import collections

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab = collections.Counter([a+b for a in A for b in B])
        return sum([ab[-(c+d)] for c in C for d in D])
if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    s = Solution()
    print(s.fourSumCount(A,B,C,D))