# Sort an Array
from typing import List


class Solution:

    def partition(self, nums, i, j):
        p = i - 1
        q = j + 1
        pivot = nums[i]
        while 1:
            while 1:
                p += 1
                if nums[p] >= pivot:
                    break
            while 1:
                q -= 1
                if nums[q] <= pivot:
                    break
            if p < q:
                tmp = nums[p]
                nums[p] = nums[q]
                nums[q] = tmp
            else:
                return q

    def quickSort(self, nums, i, j):
        if i < j:
            split = self.partition(nums, i, j)
            self.quickSort(nums, i, split)
            self.quickSort(nums, split + 1, j)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

if __name__ == '__main__':
    a = [5,2,3,1]
    s = Solution()
    s.sortArray(a)
    print(a)