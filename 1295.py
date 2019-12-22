# Find Numbers with Even Number of Digits
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            i = 1
            while n:
                n //= 10
                i += 1
            ans += i % 2
        return ans

s = Solution()
print(s.findNumbers([555,901,482,1771]))