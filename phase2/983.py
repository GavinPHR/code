#
from typing import List
import bisect

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * len(days)
        dp[0] = costs[0]
        tmp = bisect.bisect_left(days, days[0] + 7) - 1
        dp[tmp] = min(dp[tmp], costs[1])
        tmp = bisect.bisect_left(days, days[0] + 30) - 1
        dp[tmp] = min(dp[tmp], costs[2])
        for i in range(1, len(days)):
            prevVal = dp[i - 1]
            dp[i] = min(dp[i], prevVal + costs[0])
            tmp = bisect.bisect_left(days, days[i] + 7) - 1
            dp[tmp] = min(dp[tmp], prevVal + costs[1])
            tmp = bisect.bisect_left(days, days[i] + 30) - 1
            dp[tmp] = min(dp[tmp], prevVal + costs[2])
        return dp[-1]

s = Solution()
print(s.mincostTickets(
[3,12,17,32,34,37,42,43,50,53,54,55,56,57,59,60,62,63,64,66,70,71,73,79,85,87,91,95,99]
,[3,12,44]))
