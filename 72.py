# Edit Distance
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a, b = len(word1), len(word2)
        dp = [[0]*(a+1) for _ in range(b+1)]
        for j in range(a + 1):
            dp[0][j] = j
        for i in range(b + 1):
            dp[i][0] = i
        for j in range(1,a + 1):
            for i in range(1,b + 1):
                offset = 0
                if word1[j - 1] == word2[i - 1]:
                    offset = -1
                dp[i][j] = min(dp[i - 1][j], dp[i][j-1], dp[i-1][j-1]+offset) + 1
        for row in dp:
            print(row)
        return dp[-1][-1]




# word1 = "intention"
# word2 = "execution"
word1 = "horse"
word2 = "ros"
s = Solution()
print(s.minDistance(word1, word2))