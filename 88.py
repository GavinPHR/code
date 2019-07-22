# Merge Sorted Array
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = m + n
        t = [None] * l
        for i in range(m):
            t[i] = nums1[i]
        for i in range(n):
            t[m + i] = nums2[i]
        t.sort()
        for i in range(l):
            nums1[i] = t[i]
        return
        