# Find Minimum in Rotated Sorted Array
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]: return nums[l]
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])




s = Solution()
print(s.findMin([4,5,6,7,0,1,2]))