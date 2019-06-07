# Delete Columns to Make Sorted
from typing import List

class Solution:
    def inOrder(self, a: List[str]) -> bool:
        for i in range(len(a)-1):
            if ord(a[i]) > ord(a[i+1]):
                return False
        return True

    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for i in range(len(A[0])):
            a = []
            for j in range(len(A)):
                a.append(A[j][i])
            if not self.inOrder(a):
                count += 1
        return count


if __name__ == '__main__':
    a = ["cba","daf","ghi"]
    s = Solution()
    print(s.minDeletionSize(a))