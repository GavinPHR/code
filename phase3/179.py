# Largest Number
from typing import List
import functools

class Solution:
    def largestNumber(self, nums):
        class Predicate:

            def __init__(self, str):
                self.str = str

            def __lt__(self, other):
                return self.str + other.str < other.str + self.str

        strs = ''.join(sorted(map(str, nums), key=Predicate, reverse=True))
        return '0' if strs[0] == '0' else strs

s = Solution()
print(s.largestNumber([3,30,34,5,9]))
#Output: "9534330"