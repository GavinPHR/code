# Intersection of Two Arrays
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1.sort()
        nums2.sort()
        def binSearch(nums, n):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < n:
                    l = mid + 1
                elif nums[mid] > n:
                    r = mid - 1
                else:
                    return True
            return False
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in ans:
                    continue
                if binSearch(nums2, i):
                    ans.append(i)
        else:
            for i in nums2:
                if i in ans:
                    continue
                if binSearch(nums1, i):
                    ans.append(i)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.intersection([1,3,8,9,3],[1,0]))