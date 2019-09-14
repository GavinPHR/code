# Complex Number Multiplication
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
            r = len(a) - 1
            for i, n in enumerate(a):
                if n == "+":
                    a = (int(a[0:i]), int(a[i + 1:r]))
                    break
            r = len(b) - 1
            for i, n in enumerate(b):
                if n == "+":
                    b = (int(b[0:i]), int(b[i + 1:r]))
                    break
            r = a[0] * b[0] - a[1] * b[1]
            i = a[0] * b[1] + a[1] * b[0]
            return str(r) + '+' + str(i) + 'i'

s = Solution()
print(s.complexNumberMultiply("1+-1i", "1+-1i"))