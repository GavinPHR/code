# Find First and Last Position of Element in Sorted Array
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        l, r = 0, len(nums) - 1
        while True:
            mid = (l + r)//2
            val = nums[mid]
            if val == target:
                break
            elif abs(l-r) < 2:
                break
            elif val > target:
                r = mid
            else:
                l = mid
        if nums[(l+r)//2] != target:
            if nums[l] == target: return [l,l]
            if nums[r] == target: return [r,r]
            return [-1,-1]
        while nums[l] != target: l += 1
        while nums[r] != target: r -= 1
        return [l,r]


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
