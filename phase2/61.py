# Rotate List
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        if k == 0: return head
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        if l == 1: return head
        n = k % l
        if n == 0: return head
        tmp = head
        for _ in range(l - n - 1):
            tmp = tmp.next
        newstart = tmp.next
        tmp.next = None
        tmp = newstart
        while tmp.next: tmp = tmp.next
        tmp.next = head
        return newstart


s = Solution()
h = ListNode(1)
h.next = ListNode(2)
n = s.rotateRight(h, 2)
print(n.val)
print(n.next.val)
