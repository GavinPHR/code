# Reverse Linked List II
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        left = dummy
        for _ in range(m - 1): left = left.next
        right = left
        # print(left.val)
        for _ in range(n - m + 2): right = right.next
        # print(right.val)
        prev, cur, next = right, left.next, ListNode(None)
        while next != right:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        left.next = prev
        return dummy.next

def makeLinkedList(list: list) -> ListNode:
    dummy = ListNode(None)
    current = dummy
    list.reverse()
    while list:
        current.next = ListNode(list.pop())
        current = current.next
    return dummy.next

def toList(head: ListNode) -> list:
    ret = []
    while head:
        ret.append(head.val)
        head = head.next
    return ret

head = makeLinkedList([5])
s = Solution()
print(toList(s.reverseBetween(head, 1, 1)))