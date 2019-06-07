# Nth Digit
class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 0
        idx = 9 * (10 ** i) * (i + 1)
        while n - idx > 0:
            n = n - idx
            i += 1
            idx = 9 * (10 ** i) * (i + 1)
        pos = n % (i + 1)
        print(n, i, pos, sep="||")
        num = (10 ** i - 1) + n // (i + 1)
        print(num)
        return int(str(num)[~pos]) if pos == 0 else int(str(num + 1)[pos - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(671))