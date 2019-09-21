# Remove Nth Node From End of List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        d = {}
        cur = head
        i = 0
        while cur:
            d[i] = cur
            cur = cur.next
            i += 1
        i = i - n
        if d.get(i - 1, None):
            d[i - 1].next = d.get(i + 1, None)
        else:
            return head.next
        return head

