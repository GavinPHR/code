# Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastExpo(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n % 2 != 0:
                return fastExpo(x * x, n // 2) * x
            else:
                return fastExpo(x * x, n // 2)
        neg = False
        if n < 0:
            n = -n
            neg = True
        if neg:
            return 1/fastExpo(x, n)
        else:
            return fastExpo(x, n)
if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2, 10))