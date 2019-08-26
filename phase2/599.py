# Minimum Index Sum of Two Lists
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n, m = len(list1), len(list2)
        if n > m: s, c = {x:i for i, x in enumerate(list1)}, list2
        else: s, c = {x:i for i, x in enumerate(list2)}, list1
        ans, n = [], float('inf')
        for i in range(len(c)):
            if c[i] in s:
                tmp = i + s[c[i]]
                if  tmp < n:
                    ans, n = [c[i]], tmp
                elif tmp == n:
                    ans.append(c[i])
        return ans



s = Solution()
print(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))


# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]