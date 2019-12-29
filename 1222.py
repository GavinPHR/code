# Queens That Can Attack the King
from typing import List
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        s = set((queen[0], queen[1]) for queen in queens)
        ans = []
        # horizontal
        j = king[1]
        while j >= 0:
            test = (king[0], j)
            if test in s:
                ans.append(test)
                break
            j -= 1
        j = king[1]
        while j < 8:
            test = (king[0], j)
            if test in s:
                ans.append(test)
                break
            j += 1
        i = king[0]
        while i >= 0:
            test = (i, king[1])
            if test in s:
                ans.append(test)
                break
            i -= 1
        i = king[0]
        while i < 8:
            test = (i, king[1])
            if test in s:
                ans.append(test)
                break
            i += 1
        i, j = king[0], king[1]
        while i >= 0 and i < 8 and j >= 0 and j < 8:
            test = (i,j)
            if test in s:
                ans.append(test)
                break
            i -= 1
            j -= 1
        i, j = king[0], king[1]
        while i >= 0 and i < 8 and j >= 0 and j < 8:
            test = (i,j)
            if test in s:
                ans.append(test)
                break
            i += 1
            j += 1
        i, j = king[0], king[1]
        while i >= 0 and i < 8 and j >= 0 and j < 8:
            test = (i, j)
            if test in s:
                ans.append(test)
                break
            i += 1
            j -= 1
        i, j = king[0], king[1]
        while i >= 0 and i < 8 and j >= 0 and j < 8:
            test = (i, j)
            if test in s:
                ans.append(test)
                break
            i -= 1
            j += 1
        return ans
s = Solution()
queen = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king = [0,0]
print(s.queensAttacktheKing(queen, king))