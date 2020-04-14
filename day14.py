class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        sh = 0
        for right_shift, amount  in shift:
            if right_shift:
                sh += amount
            else:
                sh -= amount
        sh %= len(s)
        return s[-sh:] + s[:-sh]
        