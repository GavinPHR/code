# Degree of an Array
from typing import List
import collections

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = collections.defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        m = 0
        ans = float('inf')
        for v in sorted(d.values(), key=lambda x:-len(x)):
            if len(v) < m: break
            m = len(v)
            seg = v[-1] - v[0] + 1
            if seg < ans:
                ans = seg
        return ans


if __name__ == '__main__':
    a = [1,2,2,3,1,4,2]
    s = Solution()
    print(s.findShortestSubArray(a))