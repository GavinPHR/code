# Valid Mountain Array
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i = 1
        try:
            while A[i] > A[i - 1]: i += 1
        except IndexError:
            return False
        while i < len(A) and A[i] < A[i - 1]: i += 1
        if i == len(A): return True
        return False