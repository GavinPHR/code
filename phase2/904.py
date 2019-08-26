# Fruit Into Baskets
from typing import List
import collections

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans, q, Q = 1, collections.deque([tree[0]]), [tree[0]]
        for i in range(1, len(tree)):
            if tree[i] in Q:
                q.append(tree[i])
            elif len(Q) == 1:
                Q.append(tree[i])
                q.append(tree[i])
            else:
                ans = max(ans, len(q))
                lastSeen = q[-1]
                j = len(q) - 1
                while q[j] == lastSeen: j -= 1
                Q[Q.index(q[j])] = tree[i]
                for _ in range(j + 1): q.popleft()
                q.append(tree[i])
        ans = max(ans, len(q))
        return ans


s = Solution()
print(s.totalFruit([1,2,2]))