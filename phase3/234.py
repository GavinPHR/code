# Palindrome Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        A = []
        while head:
            A.append(head.val)
            head = head.next
        L = len(A)
        if L % 2 == 0:
            l = L // 2 - 1
            r = L // 2
        else:
            l = r = L // 2
        while l >= 0:
            if A[l] != A[r]: return False
            l -= 1
            r += 1
        return True