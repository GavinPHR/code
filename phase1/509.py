# Fibonacci Number

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        pp = 0
        p = 1
        for i in range(1, N):
            print(p)
            tmp = pp + p
            pp = p
            p = tmp
        return tmp

if __name__ == '__main__':
    s = Solution()
    print(s.fib(4))