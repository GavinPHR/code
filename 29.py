# Divide Two Integers


class Solution:
    # Binary long division
    def divide(self, a: int, b: int) -> int:
        sign = (a < 0) == (b < 0)
        a, b, r = bin(abs(a))[2:], abs(b), ""
        q = ["0" for i in range(len(a))]
        for i in range(len(a)):
            r += a[i]
            if int(r, 2) >= b:
                r = bin(int(r, 2) - b)[2:]
                q[i] = "1"
        ans = int("".join(q), 2)
        if not sign:
            ans = -ans
        return min(max(-2147483648, ans), 2147483647)


if __name__ == '__main__':
    s = Solution()
    print(s.divide(10,3))
    print(s.divide(-7,3))