# Non-overlapping Intervals
from typing import List
import collections

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x[1])
        t = intervals[0][1]
        ans = 0
        for s, e in intervals[1:]:
            if s < t:
                ans += 1
            else:
                t = e
        return ans


s = Solution()
print(s.eraseOverlapIntervals([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]))