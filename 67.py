# Add Binary

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a, 2) + int(b, 2))[2:]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        stack = []
        n, m = len(a), len(b)
        carry = False
        for i in range(-1, -min(n,m) - 1, -1):
            if carry:
                if a[i] == "1" and b[i] == "1":
                    stack.append("1")
                elif a[i] == "1" or b[i] == "1":
                    stack.append("0")
                else:
                    stack.append("1")
                    carry = False
            else:
                if a[i] == "1" and b[i] == "1":
                    stack.append("0")
                    carry = True
                elif a[i] == "1" or b[i] == "1":
                    stack.append("1")
                else:
                    stack.append("0")
        diff = n - m
        print(diff)
        if diff > 0:
            for i in range(-m - 1, -n - 1 , -1):
                if carry:
                    if a[i] == "1":
                        stack.append("0")
                    else:
                        stack.append("1")
                        carry = False
                else:
                    stack.append(a[i])
        elif diff < 0:
            for i in range(-n - 1, -m - 1 , -1):
                if carry:
                    if b[i] == "1":
                        stack.append("0")
                    else:
                        stack.append("1")
                        carry = False
                else:
                    stack.append(b[i])
        if carry: stack.append("1")
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans
s = Solution()
print(s.addBinary(a = "1010", b = "101"))