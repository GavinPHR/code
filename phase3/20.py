# Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = {"(", "[", "{"}
        right = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if not stack and c in right:
                return False
            elif not stack or c in left:
                stack.append(c)
            elif stack[-1] != right[c]:
                return False
            else:
                stack.pop()
        if not stack: return True
        else: return False
