# Insert Interval
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            intervals.append(newInterval)
            return intervals
        l, r = newInterval[0], newInterval[1]
        l_p, r_p = -1, -1
        L, R = None, None
        for i in range(len(intervals)):
            if l >= intervals[i][0]:
                l_p += 1
            if r >= intervals[i][0]:
                r_p += 1
        if l_p != -1:
            if l <= intervals[l_p][1]:
                L = intervals[l_p][0]
            else:
                l_p += 1
                L = l
        else:
            L = l
        if l_p == len(intervals):
            intervals.append(newInterval)
            return intervals
        if r_p != -1:
            if r <= intervals[r_p][1]:
                R = intervals[r_p][1]
            else:
                R = r
        else:
            R = r
        ans = []
        flag = True
        for i in list(range(-1, len(intervals))):
            if l_p > r_p:
                if i == r_p:
                    ans.append([L, R])
            if i >= l_p and i <= r_p and flag:
                ans.append([L, R])
                flag = False
            elif i > r_p or i < l_p:
                if i != -1:
                    ans.append(intervals[i])
        return ans



if __name__ == '__main__':
    a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    b = [5.5, 8]
    s = Solution()
    print(s.insert([],[6,6]))