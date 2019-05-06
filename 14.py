# Longest Common Prefix
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        i = 0
        while True:
            try:
                tmp = [x[i] for x in strs]
            except Exception:
                return strs[0][:i]
            for j in range(1, len(strs)):
                if tmp[j - 1] != tmp[j]:
                    return strs[0][:i]
            i += 1
        return
if __name__ == '__main__':
    a = ["flower", "flow", "flight"]
    b = ["dog","racecar","car"]
    s = Solution()
    print(s.longestCommonPrefix([]))