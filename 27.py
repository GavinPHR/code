# Remove Element
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = -1
        for i, n in enumerate(nums):
            if n == val:
                continue
            elif i-1 == end:
                end += 1
            else:
                end += 1
                nums[end] = n
        return end + 1
