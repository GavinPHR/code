# Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {(0,1):"M",
             (1,5):"D",
             (1,1):"C",
             (2,5):"L",
             (2,1):"X",
             (3,5):"V",
             (3,1):"I",}
        denom = 1000
        ans = []
        while num:
            ans.append(num // denom)
            num %= denom
            denom //= 10
        for i, n in enumerate(ans):
            if n < 4:
                ans[i] = d[(i,1)] * n
            elif n == 4:
                ans[i] = d[(i,1)] + d[(i,5)]
            elif n < 9:
                ans[i] = d[(i,5)] + d[(i,1)]*(n-5)
            else:
                ans[i] = d[(i,1)] + d[(i - 1, 1)]
        return "".join(ans)

s = Solution()
print(s.intToRoman(1994))