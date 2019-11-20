# Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        ln, lh = len(needle), len(haystack)
        if ln > lh: return -1
        for i in range(lh-ln+1):
            flag = True
            idx = i
            for j in range(ln):
                if haystack[idx] != needle[j]:
                    flag = False
                    break
                idx += 1
            if flag:
                return i
        return -1

s = Solution()
print(s.strStr("mississippi","mississippi"))