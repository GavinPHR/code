# Find Peak Element
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(-float('inf'))
        for i in range(n):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
        return