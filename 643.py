# Maximum Average Subarray I
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        partial = sum(x for x in nums[0:k])
        m = partial
        for r in range(k, len(nums)):
            partial += nums[r] - nums[r - k]
            m = max(m, partial)
        return m / k


if __name__ == '__main__':
    a = [1,12,-5,-6,50,3]
    k = 4
    s = Solution()
    print(s.findMaxAverage(a,k))