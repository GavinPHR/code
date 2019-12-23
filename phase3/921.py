# Minimum Add to Make Parentheses Valid
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        ans = 0
        for c in S:
            if c == "(": count += 1
            elif c == ")" and count == 0: ans += 1
            else: count -= 1
        ans += count
        return ans