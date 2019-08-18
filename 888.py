# Fair Candy Swap
from typing import List

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B)) // 2
        B = set(B)
        for n in A:
            if n - diff in B:
                return (n, n - diff)
