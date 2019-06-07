# Excel Sheet Column Number
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        if s == "": return 0
        base = 1
        for i in range(len(s) - 1, -1, -1):
            ans += (ord(s[i]) - 64) * base
            base *= 26
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber("ZY"))