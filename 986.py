# Interval List Intersections
from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B: return []
        which = A[-1][1] >= B[-1][1]
        head = A.pop() if which else B.pop()
        ans = []
        while A and B:
            if which:
                current = B.pop()
                if current[0] > head[1]:
                    continue
                elif current[0] >= head[0]:
                    ans.append([current[0], min(current[1], head[1])])
                elif current[1] >= head[0]:
                    ans.append([head[0], min(current[1], head[1])])
                    head = current
                    which = False
                else:
                    head = current
                    which = False
            else:
                current = A.pop()
                if current[0] > head[1]:
                    continue
                elif current[0] >= head[0]:
                    ans.append([current[0], min(current[1], head[1])])
                elif current[1] >= head[0]:
                    ans.append([head[0], min(current[1], head[1])])
                    head = current
                    which = True
                else:
                    head = current
                    which = True
        while A:
            if which: break
            current = A.pop()
            if current[0] > head[1]:
                continue
            elif current[0] >= head[0]:
                ans.append([current[0], min(current[1], head[1])])
            elif current[1] >= head[0]:
                ans.append([head[0], min(current[1], head[1])])
                break
            else:
                break

        while B:
            if not which: break
            current = B.pop()
            if current[0] > head[1]:
                continue
            elif current[0] >= head[0]:
                ans.append([current[0], min(current[1], head[1])])
            elif current[1] >= head[0]:
                ans.append([head[0], min(current[1], head[1])])
                break
            else:
                break
        return ans[::-1]

s = Solution()
A = [[6,7],[8,13],[15,19]]
B = [[1,2],[4,5],[11,13],[15,16],[17,19]]
print(s.intervalIntersection(A, B))