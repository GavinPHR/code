# Find Pivot Index
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        s = sum(nums)
        l = 0
        s -= nums[0]
        if s == 0:
            return 0
        for i in range(1, len(nums)):
            s -= nums[i]
            l += nums[i - 1]
            if s == l:
                return i
        return -1
