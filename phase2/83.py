# Remove Duplicates from Sorted List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return
        prev = head
        tmp = head.next
        while tmp:
            if tmp.val == prev.val:
                tmp = tmp.next
                continue
            prev.next = tmp
            prev = tmp
        prev.next = None
        return head

s = Solution()
l = ListNode(1)
l.next = ListNode(1)
l.next.next = ListNode(2)
print(s.deleteDuplicates(l).next.val)