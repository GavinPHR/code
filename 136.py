# Single Number
from typing import List
import functools

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda a,b: a^b, nums)

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))