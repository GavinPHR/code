# Top K Frequent Elements
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        heap = []
        prev, count = nums[0], 0
        for i in range(len(nums)):
            if nums[i] == prev:
                count += 1
                prev = nums[i]
            else:
                heapq.heappush(heap, (-count, prev))
                count = 1
                prev = nums[i]
        heapq.heappush(heap, (-count, prev))
        return [heapq.heappop(heap)[1] for i in range(k)]

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2))