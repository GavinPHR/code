# Monotone Increasing Digits
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        N = list(str(N))
        i = 0
        while i < len(N) - 1:
            if N[i] > N[i + 1]:
                break
            i += 1
        if i == len(N) - 1: return int("".join(N))
        N[i] = str(int(N[i]) - 1)
        for j in range(i + 1, len(N)):
            N[j] = '9'
        while i > 0 and N[i] < N[i - 1]:
            N[i - 1] = N[i]
            N[i] = '9'
            i -= 1
        return int("".join(N))


        # for n in N:
        #     if n == "0"
        #     count = 0
        #     tmp = None
        #     while stack and stack[-1] > n:
        #         count += 1
        #         tmp = stack.pop()
        #     if tmp :
        #         stack.append(str(int(tmp) - 1))
        #     else:
        #         stack.append(n)
        #     for _ in range(count): stack.append("9")
        # return int("".join(stack))

s = Solution()
print(s.monotoneIncreasingDigits(1234))