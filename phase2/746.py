# Min Cost Climbing Stairs
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n < 2: return 0
        acc = [0] * n
        acc[0], acc[1] = cost[0], cost[1]
        for i in range(2, n):
            acc[i] = cost[i] + min(acc[i - 2], acc[i - 1])
        return min(acc[n - 2], acc[n - 1])