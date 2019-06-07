# Evaluate Reverse Polish Notation

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif c == "-":
                fst = int(stack.pop())
                stack.append(int(stack.pop()) - fst)
            elif c == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif c == "/":
                flag = False
                fst = int(stack.pop())
                if fst < 0:
                    flag = not flag
                    fst = abs(fst)
                snd = int(stack.pop())
                if snd < 0:
                    flag = not flag
                    snd = abs(snd)
                tmp = - (snd // fst) if flag else snd // fst
                stack.append(tmp)
            else:
                stack.append(c)
        return int(stack.pop())

if __name__ == '__main__':
    a = ["2", "1", "+", "3", "*"]
    b = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    s = Solution()
    print(s.evalRPN(b))