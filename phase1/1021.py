# Remove Outermost Parentheses

class Solution:
    stack: list = []
    count: int = 0

    def push(self, c: str):
        if not self.stack:
            self.stack.append(c)
        else:
            tmp = self.stack.pop()
            if tmp == "(" and c == ")" :
               return
            self.stack.append(tmp)
            self.stack.append(c)

    def removeOuterParentheses(self, S: str) -> str:
        pos = []
        for c in S:
            self.push(c)
            self.count += 1
            if not self.stack:
                pos.append(self.count)
        ret = ""
        j = 0
        for i in pos:
            ret += S[j+1:i-1]
            j = i
        return ret

if __name__ == '__main__':
    str = "(()())(())"
    s = Solution()
    res = s.removeOuterParentheses(str)
    print(res)