# Shortest Distance to a Character
from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        def updatePrev():
            count = 1
            for i in range(pR - 1, pL, -1):
                if ans[i] > count:
                    ans[i] = count
                    count += 1
                else:
                    return
        ans = [float('inf')] * len(S)
        pL = -1
        pR = 0
        while pR != len(S):
            if S[pR] != C:
                if pL != -1:
                    ans[pR] = ans[pR - 1] + 1
                pR += 1
                continue
            ans[pR] = 0
            updatePrev()
            pL = pR
            pR += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.shortestToChar("loveleetcode", 'e'))