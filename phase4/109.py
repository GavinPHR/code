# Convert Sorted List to Binary Search Tree
# Simulate inorder traversal

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def cut(self, head: ListNode) -> List[ListNode]:
    #     prev, slow, fast = None, head, head
    #     while fast and fast.next:
    #         prev = slow
    #         slow = slow.next
    #         fast = fast.next.next
    #     prev.next = None
    #     return [head, slow, slow.next]
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        count = 0
        p = head
        while p:
            count += 1
            p = p.next
        def recursive(l, r):
            nonlocal head
            if l > r: return None
            mid = (l+r+1)//2
            left = recursive(l, mid - 1)
            m = TreeNode(head.val)
            head = head.next
            right = recursive(mid + 1, r)
            m.left = left
            m.right = right
            return m
        return recursive(0, count - 1)
    
            