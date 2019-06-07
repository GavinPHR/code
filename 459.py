# Repeated Substring Pattern
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1: return False
        for i in range(2, n + 1):
            if n % i != 0: continue
            l = n // i
            if s[0] != s[l]: continue
            flag = True
            for j in range(0, i - 1):
                print(s[j * l: (j + 1) * l])
                print(s[(j + 1) * l: (j + 2) * l])
                if s[j * l: (j + 1) * l] != s[(j + 1) * l: (j + 2) * l]:
                    flag = False
                    break
            if flag: return True
        return False

s = Solution()
print(s.repeatedSubstringPattern("bb"))
