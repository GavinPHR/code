# Search a 2D Matrix
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        n, m = len(matrix), len(matrix[0])
        l,r  = 0, n*m-1
        while l <= r:
            mid = (l+r)//2
            val = matrix[mid//m][mid%m]
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True
        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]



s = Solution()
print(s.searchMatrix(matrix, 3))