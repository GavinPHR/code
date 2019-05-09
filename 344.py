# Reverse String
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        if s == []: return
        for i in range(len(s) // 2):
            tmp = s[i]
            s[i] = s[~i]
            s[~i] = tmp
        return

if __name__ == '__main__':
    a = ["h","e","l","l","o"]
    s = Solution()
    s.reverseString(a)
    print(a)

