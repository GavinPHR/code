# Spiral Matrix III
from typing import List


class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def inM(a, b):
            if a >= 0 and a < R and b >=0 and b < C:
                return True
            else:
                return False

        def spiral(a, b, side):
            for i in range(4):
                #Right side
                if i == 0:
                    for j in range(side - 1):
                        a += 1
                        if inM(a, b):
                            ans.append([a, b])
                #Bottom side
                elif i == 1:
                    for j in range(side - 1):
                        b -= 1
                        if inM(a, b):
                            ans.append([a, b])
                #Left side
                elif i == 2:
                    for j in range(side - 1):
                        a -= 1
                        if inM(a, b):
                            ans.append([a, b])
                #Top Side
                else:
                    for j in range(side - 1):
                        b += 1
                        if inM(a, b):
                            ans.append([a, b])
        N = R * C
        ans = [[r0, c0]]
        side = 3
        while len(ans) != N:
            r0 -= 1
            c0 += 1
            spiral(r0, c0, side)
            side += 2
        return ans
if __name__ == '__main__':
    s = Solution()
    print(s.spiralMatrixIII(1, 4, 0, 0))