# Plus One
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] != 10:
            return digits
        ans = []
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10:
                ans.append(0)
                digits[i - 1] += 1
            else:
                ans.append(digits[i])
        if ans[-1] == 0:
            ans.append(1)
        ans.reverse()
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9,9,9]))