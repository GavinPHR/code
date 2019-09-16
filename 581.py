# Shortest Unsorted Continuous Subarray
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        c = sorted(nums)
        l = 0
        while l < len(nums):
            if nums[l] != c[l]: break
            l += 1
        if l == len(nums): return 0
        r = len(nums) - 1
        while r > -1:
            if nums[r] != c[r]: break
            r -= 1
        return r - l + 1

