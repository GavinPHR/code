# Maximum Average Subarray I
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        tmp = ans
        for i in range(k, len(nums)):
            tmp = tmp - nums[i - k] + nums[i]
            ans = max(ans, tmp)
        return ans / k


if __name__ == '__main__':
    a = [1,12,-5,-6,50,3]
    k = 4
    s = Solution()
    print(s.findMaxAverage(a,k))