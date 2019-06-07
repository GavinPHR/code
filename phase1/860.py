# Lemonade Change
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = [0, 0]
        for i in bills:
            if i == 5:
                d[0] += 1
            elif i == 10:
                if not d[0]: return False
                d[1] += 1
                d[0] -= 1
            elif i == 20:
                if d[0] and d[1]:
                    d[0] -= 1
                    d[1] -= 1
                    continue
                elif d[0] > 2:
                    d[0] -= 3
                    continue
                return False
        return True

if __name__ == '__main__':
    a = [5,5,10,10,20]
    s = Solution()
    print(s.lemonadeChange(a))
