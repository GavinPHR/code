# Maximum Subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        ans = nums[0]
        minSeen = nums[0]
        for i in range(1, n):
            nums[i] += nums[i - 1]
            if nums[i] > ans:
                ans = nums[i]
            if nums[i] - minSeen > ans:
                ans = nums[i] - minSeen
            if nums[i] < minSeen:
                minSeen = nums[i]
        return ans

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))