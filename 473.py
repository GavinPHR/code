# Matchsticks to Square
from typing import List
import time

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        s = sum(nums)
        if len(nums) < 4 or s % 4 != 0:
            return False
        target = s // 4
        def recur(count, one, two, three, four):
            print(count, one, two, three, four, sep="  ")
            if one > target or two > target or three > target or four > target:
                return False
            if count == len(nums) and one == target \
                and two == target and three == target \
                and four == target:
                return True
            newcount = count + 1
            if not (one or two or three or four):
                return recur(newcount, one + nums[count], two, three, four)
            if not (two or three or four):
                o = recur(newcount, one + nums[count], two, three, four)
                if o:
                    return True
                t = recur(newcount, one, two + nums[count], three, four)
                if t:
                    return True
                return False
            if not (three or four):
                o = recur(newcount, one + nums[count], two, three, four)
                if o:
                    return True
                t = recur(newcount, one, two + nums[count], three, four)
                if t:
                    return True
                th = recur(newcount, one, two, three + nums[count], four)
                if th:
                    return True
                return False
            o = recur(newcount, one + nums[count], two, three, four)
            if o: return True
            t = recur(newcount, one, two + nums[count], three, four)
            if t: return True
            th = recur(newcount, one, two, three + nums[count], four)
            if th: return True
            f = recur(newcount, one, two, three, four + nums[count])
            if f: return True
            return False
        nums.sort(reverse=True)
        return recur(0, 0, 0, 0, 0)



if __name__ == '__main__':
    s = Solution()
    print(s.makesquare(
[5,5,5,5,12,4,4,4,4,4,3,3,3,3,4]))
