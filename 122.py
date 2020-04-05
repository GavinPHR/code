class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        prices.append(-float('inf'))
        prices = [float('inf')] + prices
        i = 0
        while i < len(prices)-1:
            if prices[i] > prices[i-1] or prices[i] > prices[i+1]:
                i += 1
                continue
            b = prices[i]
            while i < len(prices) and prices[i+1] >= prices[i]:
                i += 1
            ans += (prices[i]-b)
            i += 1
        return ans
            
            
        