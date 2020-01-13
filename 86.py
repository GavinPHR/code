# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None: return head
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        cur = head
        while cur and cur.val < x:
            prev = cur
            cur = cur.next
        if not cur: return head
        insert = prev
        while cur:
            if cur.val >= x:
                prev = cur
                cur = cur.next
                continue
            next = cur.next
            after = insert.next
            insert.next = cur
            insert = cur
            cur.next = after
            prev.next = next
            cur = next
        return dummy.next

t = ListNode(2)
t.next = ListNode(1)
s = Solution()
print(s.partition(t, 2))