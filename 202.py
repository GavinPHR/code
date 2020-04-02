# Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = sum(int(c)**2 for c in str(slow))
            fast = sum(int(c)**2 for c in str(fast))
            fast = sum(int(c)**2 for c in str(fast))
            
            if slow == 1 or fast == 1:
                return True
            elif slow == fast:
                return False
        return True



