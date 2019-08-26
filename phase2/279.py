# Perfect Squares

class Solution:
    dp = [0]
    def numSquares(self, n: int) -> int:
        while len(self.dp) <= n:
            self.dp.append(min(self.dp[-i*i] for i in range(1,int(len(self.dp)**.5)+1)) + 1)
        return self.dp[n]

s = Solution()
print(s.numSquares(12))