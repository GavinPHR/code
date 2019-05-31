# Clumsy Factorial
class Solution:
    def clumsy(self, N: int) -> int:
        def td(n1, n2, n3):
            if n2 < 1:
                n2 = 1
            if n3 < 1:
                n3 = 1
            return n1 * n2 // n3
        ans = td(N, N-1, N-2)
        i = N - 3
        f1 = False
        while i > 0:
            print(i, ans)
            if f1:
                ans -= td(i, i-1, i-2)
                i -= 3
                f1 = False
            else:
                ans += i
                i -= 1
                f1 = True

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.clumsy(1))