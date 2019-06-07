# Majority Element
from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        return count.most_common(1)[0][0]

if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))