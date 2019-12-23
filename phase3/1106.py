# Parsing A Boolean Expression
#
# "t", evaluating to True;
# "f", evaluating to False;
# "!(expr)", evaluating to the logical NOT of the inner expression expr;
# "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
# "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...


class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        if exp == 't': return True
        if exp == 'f': return False
        if exp[0] == '!': return not self.parseBoolExpr(exp[2:len(exp)-1])
        op = exp[0]
        exp = exp[2:len(exp)-1]
        ans = []
        count = 0
        prev = 0
        for i, n in enumerate(exp):
            if n == '(': count += 1
            elif n == ')': count -= 1
            elif n == ',' and count == 0:
                ans.append(exp[prev:i])
                prev = i + 1
        ans.append(exp[prev:])
        if op == '&': return all(self.parseBoolExpr(e) for e in ans)
        elif op == '|': return any(self.parseBoolExpr(e) for e in ans)

s = Solution()
print(s.parseBoolExpr("|(f,t)"))