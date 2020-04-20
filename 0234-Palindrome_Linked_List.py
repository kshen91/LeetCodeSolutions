# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# O(n) time complexity, O(1) space complexity

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        secondHalfReverseHead = self.reverseList(slow.next)
        
        while secondHalfReverseHead:
            if head.val != secondHalfReverseHead.val:
                return False
            head = head.next
            secondHalfReverseHead = secondHalfReverseHead.next
            
        return True
        
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        
        return prev
