# Powerful Integers
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x == 1 and y == 1 and bound >= 2:
            return [2]
        if x == 1:
            i = 0
            ans = []
            while y ** i < bound:
                ans.append(y ** i + 1)
                i += 1
            return ans
        if y == 1:
            i = 0
            ans = []
            while x ** i < bound:
                ans.append(x ** i + 1)
                i += 1
            return ans
        ans = set()
        i = 0
        while True:
            if x ** i >= bound:
                break
            j = 0
            while True:
                tmp = x ** i + y ** j
                if tmp <= bound:
                    ans.add(tmp)
                    j += 1
                else:
                    break
            i += 1
        return list(ans)

if __name__ == '__main__':
    s = Solution()
    print(s.powerfulIntegers(2,1,10))