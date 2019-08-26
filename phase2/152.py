# Maximum Product Subarray
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m, s = [None] * len(nums), [None] * len(nums)
        m[0], s[0] = nums[0], nums[0]
        for i, n in enumerate(nums):
            if i == 0: continue
            tmp1, tmp2 = n * m[i - 1], n * s[i - 1]
            m[i] = max(tmp1, tmp2, n)
            s[i] = min(tmp1, tmp2, n)
        return max(m)

s = Solution()
print(s.maxProduct([2,3,-2,4]))