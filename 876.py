# Middle of the Linked List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = head
        list = []
        while node:
            list.append(node)
            node = node.next
        return list[len(list) // 2].val

    def middleNode1(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val

if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    l.next.next.next.next.next = ListNode(6)


    s = Solution()
    print(s.middleNode1(l))