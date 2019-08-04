# Height Checker
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        i = iter(sorted(heights))
        ans = 0
        for n in heights:
            if n != next(i): ans += 1
        return ans