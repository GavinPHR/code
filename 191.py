# 191. Number of 1 Bits
class Solution(object):
    def hammingWeight(self, n):
        ans = 0
        i = 2 ** 31
        while n:
            if n // i != 0:
                ans += 1
                n -= i
            i //= 2
        return ans

# Trick
# class Solution(object):
#     def hammingWeight(self, n):
#         ans = 0
#         while n:
#             ans += 1
#             n &= (n-1)
#         return ans

s = Solution()
print(s.hammingWeight(11))
