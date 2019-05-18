# Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x == 1: return 1
        i = x // 2
        while True:
            if i * i <= x:
                break
            i //= 2
        while True:
            if i * i > x:
                break
            i += 1
        print(i)
        return (i-1) ** 2

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(2147395599))