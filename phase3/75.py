# Sort Colors
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3
        for n in nums:
            count[n - 1] += 1
        i = 0
        for _ in range(count[0]):
            nums[i] = 0
            i += 1
        for _ in range(count[1]):
            nums[i] = 1
            i += 1
        for _ in range(count[2]):
            nums[i] = 2
            i += 1
        return

s = Solution()
l = [2,0,2,1,1,0]
s.sortColors(l)
print(l)