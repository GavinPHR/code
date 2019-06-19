# Friends Of Appropriate Ages
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        p = len(ages) - 1
        prev, count = None, 0
        ans = 0
        for i in range(len(ages) - 1, -1, -1):
            if ages[i] == prev:
                count += 1
            else:
                prev = ages[i]
                count = 0
            lo = ages[i] / 2 + 7
            if p > i: p = i
            while p > 0 and ages[p - 1] > lo:
                p -= 1
            ans += (i - p) + (count if ages[i] > lo else 0)
        return ans

s = Solution()
print(s.numFriendRequests([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]))