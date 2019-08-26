# N-th Tribonacci Number
class Solution:
    _dp = [0, 1, 1]
    def tribonacci(self, n: int) -> int:
        dp = self._dp
        if len(dp) < n + 1:
            i = len(dp) - 1
            while i != n:
                t = dp[-1] + dp[-2] + dp[-3]
                dp.append(t)
                i += 1
        return dp[n]

s = Solution()
print(s.tribonacci(25))