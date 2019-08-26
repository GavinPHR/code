# Assign Cookies

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0 or len(g) == 0: return 0
        g.sort()
        s.sort(reverse=True)
        ans = 0
        for n in g:
            while s and s[-1] < n :
                s.pop()
            if not s: break
            ans += 1
            s.pop()
        return ans

s = Solution()
print(s.findContentChildren([1,2], [1,2,3]))
