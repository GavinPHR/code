# Palindrome Pairs
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        def isPalin(left, right):
            tot = "".join([left, right])
            l ,r = 0, len(tot) - 1
            while l < r:
                if tot[l] != tot[r]: return False
                l += 1
                r -= 1
            return True
        for i in range(len(words)):
            words[0], words[i] = words[i], words[0]
            for j in range(1, len(words)):
                if isPalin(words[0], words[j]):
                    ans.append([i, j if j != i else 0])
            words[0], words[i] = words[i], words[0]
        return ans

s = Solution()
print(s.palindromePairs(["bat","tab","cat"]))