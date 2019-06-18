# Largest Number At Least Twice of Others
from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 1
        if nums[0] > nums[1]:
            ll, l = (nums[0], 0), (nums[1], 1)
        else:
            ll, l = (nums[1], 1), (nums[0], 0)
        for i in range(2, n):
            if nums[i] > ll[0]:
                l, ll = ll, (nums[i], i)
            elif nums[i] > l[0]:
                l = (nums[i], i)
            else:
                continue
        return ll[1] if ll[0] >= 2 * l[0] else -1
