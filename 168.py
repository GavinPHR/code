# Excel Sheet Column Title

class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n:
            n -= 1
            ans.append(chr(65+n%26))
            n //= 26
        ans.reverse()
        return "".join(ans)

s = Solution()
print(s.convertToTitle(701))