# Maximum Number of Events That Can Be Attended
from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events: return 0
        q = []
        events.sort(reverse=True, key=lambda x: (x[0], x[1]))
        ans = 0
        for day in range(1, 100001):
            while q and q[0] < day:
                heapq.heappop(q)
            while events and events[-1][0] == day:
                heapq.heappush(q, events.pop()[-1])
            if q:
                heapq.heappop(q)
                ans += 1
        return ans




s = Solution()
print(s.maxEvents([[1,2]]))