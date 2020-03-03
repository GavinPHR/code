# Rotate String

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        a, b = len(A), len(B)
        if a != b: return False
        match = False
        for i in range(a):
            match_inner = True
            for j in range(b):
                if A[(i+j)%a] != B[j]:
                    match_inner = False
                    break
            if match_inner:
                match = True
                break
        return match if A else True
    
    
# O(n^2) above

# can check instead B is a substring of A+A
# KMP O(n) or rolling hash O(n)