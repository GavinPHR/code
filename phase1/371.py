# Sum of Two Integers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            c = a & b
            c &= 2 ** 32 - 1
            a ^= b
            b = c << 1
            a &= 2 ** 32 - 1
            b &= 2 ** 32 - 1
        return a if a <= 0x7fffffff else ~(a ^ 0xffffffff)


if __name__ == '__main__':
    s = Solution()
    print(s.getSum(-4,3))