# Kth Largest Element in an Array
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if 2 * k > len(nums):
            heapq.heapify(nums)
            k = len(nums) - k + 1
            for i in range(k - 1):
                heapq.heappop(nums)
            return heapq.heappop(nums)
        else:
            nums = [-x for x in nums]
            heapq.heapify(nums)
            for i in range(k - 1):
                heapq.heappop(nums)
            return -heapq.heappop(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))