# Swap Nodes in Pairs
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        cur = ListNode(None)
        dummyhead = cur
        cur.next = head
        while cur.next and cur.next.next:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = cur.next.next
            cur.next.next = tmp
            cur = cur.next.next
        return dummyhead.next