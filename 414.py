# Third Maximum Number
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a,b,c = -float('inf'),-float('inf'),-float('inf')
        nums = list(set(nums))
        for n in nums:
            if n > a:
                c = b
                b = a
                a = n
            elif n > b:
                c = b
                b = n
            elif n > c:
                c = n
        return c if c != -float('inf') else a