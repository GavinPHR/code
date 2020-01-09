# Trapping Rain Water
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3: return 0
        left, right = -1, n
        maxL, maxR = 0, 0
        ans = 0
        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                ans += maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR, height[right])
                ans += maxR - height[right]
        return ans


s = Solution()
print(s.trap([5,2,1,2,1,5]))


