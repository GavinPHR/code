#  Positions of Large Groups
from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        prev, count, ans = S[0], 1, []
        for i in range(1, len(S)):
            if S[i] != prev:
                if count > 2:
                    ans.append([i - count, i - 1])
                prev, count = S[i], 1
                continue
            count += 1
        if count > 2:
            ans.append([len(S) - count, len(S) - 1])
        return ans

s = Solution()
print(s.largeGroupPositions("abc"))