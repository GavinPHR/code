# Walking Robot Simulation
from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        x, y = 0, 0
        dir = 0
        obs = set((x,y) for x,y in obstacles)
        for n in commands:
            if n == -2:
                dir = (dir-1) % 4
            elif n == -1:
                dir = (dir+1) % 4
            elif dir == 0:
                for i in range(n):
                    if (x,y + 1) in obs:
                        break
                    y += 1
                    ans = max(x**2 + y**2, ans)
            elif dir == 1:
                for i in range(n):
                    if (x+1,y) in obs:
                        break
                    x += 1
                    ans = max(x ** 2 + y ** 2, ans)
            elif dir == 2:
                for i in range(n):
                    if (x,y - 1) in obs:
                        break
                    y -= 1
                    ans = max(x ** 2 + y ** 2, ans)
            elif dir == 3:
                for i in range(n):
                    if (x-1,y) in obs:
                        break
                    x -= 1
                    ans = max(x ** 2 + y ** 2, ans)
        return ans



s = Solution()
print(s.robotSim([4,-1,4,-2,4], [[2,4]]))