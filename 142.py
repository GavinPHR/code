# Linked List Cycle II
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        slow, fast = head, head
        try:
            while True:
                slow = slow.next
                fast = fast.next.next
                if slow == fast: break
        except Exception:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
