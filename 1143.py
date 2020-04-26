class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text1)+1)
        for i in range(len(text2)):
            row = [0] * (len(text1)+1)
            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    row[j+1] = dp[j]+1
                else:
                    row[j+1] = max(row[j], dp[j+1])
            dp = row
        return dp[-1]