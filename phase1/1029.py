# Two City Scheduling
from typing import List
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        a, b = [], []
        for l, r in costs:
            if l < r:
                a.append(r - l)
                ans += l
            else:
                b.append(l - r)
                ans += r
        print(a, b, ans)
        diff = len(a) - len(b)
        if diff < 0:
            b.sort()
            for i in range(abs(diff) // 2):
                ans += b[i]
            return ans
        else:
            a.sort()
            for i in range(diff // 2):
                ans += a[i]
            return ans


if __name__ == '__main__':
    a = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    s = Solution()
    print(s.twoCitySchedCost(a))