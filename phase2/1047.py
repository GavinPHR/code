# Remove All Adjacent Duplicates In String
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if not stack:
                stack.append(c)
            elif c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
