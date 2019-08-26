# Largest Rectangle in Histogram
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        if not heights: return 0
        if l == 1: return heights[0]
        ans = 0
        #monotonic stack
        stack = [-1]
        heights.append(0)
        for i in range(l + 1):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                print(stack)
                w = i - stack[-1] - 1
                area = h * w
                if area > ans: ans = area
            stack.append(i)
        return ans



s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
