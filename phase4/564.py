# Find the Closest Palindrome
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        t = int(n)
        if t == 0: return '1'
        elif t < 10: return str(t-1)
        elif t == 10 or t == 11: return '9'
        s = set()
        l = len(n)
        leftStr = n[:(l-1)//2+1]
        # print(leftStr,n)
        left = int(leftStr)
        for i in -1, 0, 1:
            tmp = left + i
            tmpStr = str(tmp)
            if len(leftStr) > len(tmpStr):
                s.add((int('9' * (l-1)),i))
            elif len(leftStr) < len(tmpStr):
                s.add((int('1' + '0'*(l-1)+'1'),i))
            else:
                if l % 2 == 0:
                    s.add((int("".join(tmpStr + tmpStr[::-1])),i))
                else:
                    s.add((int("".join(tmpStr + tmpStr[::-1][1:])),i))
        if (t,0) in s: s.remove((t,0))
        return str(min(s, key=lambda x: (abs(int(n)-int(x[0])), x[1]))[0])

s = Solution()
print(s.nearestPalindromic('1'))
print(s.nearestPalindromic('10'))
print(s.nearestPalindromic('123'))
print(s.nearestPalindromic('99'))
print(s.nearestPalindromic('11011'))
print(s.nearestPalindromic('100000'))