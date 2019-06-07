# Best Time to Buy and Sell Stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        max = prices[-1]
        maxes = [max]
        for i in range(len(prices) - 2, 0, -1):
            if prices[i] > max:
                max = prices[i]
            maxes.append(max)
        max = 0
        for i in range(len(prices) - 1):
            if maxes[~i] - prices[i] > max:
                max = maxes[~i] - prices[i]
        return max


if __name__ == '__main__':
    a = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(a))