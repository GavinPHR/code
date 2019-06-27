# Word Break
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        canBeBuilt = [True] + [False] * len(s)# ""
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if canBeBuilt[j] and s[j:i] in wordDict:
                    canBeBuilt[i] = True
                    break
        return canBeBuilt[-1]

s = Solution()
print(s.wordBreak("ab", ["a", "b"]))