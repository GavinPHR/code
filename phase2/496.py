# Next Greater Element I
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2: return []
        d = dict()
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    d[nums2[i]] = nums2[j]
                    break
        ans = [d.get(x, -1) for x in nums1]
        return ans

s = Solution()
print(s.nextGreaterElement([2,4], [1,2,3,4]))
