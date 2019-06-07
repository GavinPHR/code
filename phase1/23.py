# Merge k Sorted Lists
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def minimum(lists):
            min, index = float('inf'), -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if lists[i].val < min:
                    min = lists[i].val
                    index = i
            return lists[index], index

        ans = ListNode(None)
        cur = ans
        while any(lists):
            tmpnode, index = minimum(lists)
            cur.next = tmpnode
            cur = cur.next
            lists[index] = tmpnode.next
        return ans.next




if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    s = Solution()
    h = s.mergeKLists([l1,l2])
    while h:
        print(h.val)
        h = h.next