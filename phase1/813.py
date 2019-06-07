# Largest Sum of Averages
from typing import List
#https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-813-largest-sum-of-averages/
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        dp = [[None for _ in range(len(A))] for _  in range(K) ]
        partial = 0
        for i in range(len(A)):
            partial += A[i]
            dp[0][i] = partial / (i + 1)
        for k in range(1, K):
            for i in range(k, len(A)):
                max = -1
                for j in range(k - 1, i):
                    tmp = dp[k - 1][j] + sum(A[j + 1:i + 1]) / (i - j)
                    if tmp > max:
                        max = tmp
                dp[k][i] = max
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    a = [4,1,7,5,6,2,3]
    print(s.largestSumOfAverages(a, 4))