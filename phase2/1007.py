# Minimum Domino Rotations For Equal Row
from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        t, b, n, ft, fb = A[0], B[0], len(A), 0, 0
        for x, y in zip(A, B):
            if x == t: continue
            if y == t:
                ft += 1
                continue
            ft = float('inf')
            break
        if ft != float('inf'):
            _ft = 0
            for x, y in zip(A, B):
                if y == t: continue
                if x == t:
                    _ft += 1
                    continue
            ft = min(ft, _ft)
        for x, y in zip(A, B):
            if y == b: continue
            if x == b:
                fb += 1
                continue
            fb = float('inf')
            break
        if fb != float('inf'):
            _fb = 0
            for x, y in zip(A, B):
                if x == b: continue
                if y == b:
                    _fb += 1
                    continue
            fb = min(fb, _fb)
        print(n, ft, fb)
        if ft == float('inf') and fb == float('inf'): return -1
        return min(ft, fb)

s = Solution()
A = [1,1,1,2,1,1,1,2,1,1,2,1,1,2,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,2,1,1,1]
B = [2,2,1,1,1,1,2,1,2,2,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,2]
print(list(zip(A,B)))
print(s.minDominoRotations(A,B))