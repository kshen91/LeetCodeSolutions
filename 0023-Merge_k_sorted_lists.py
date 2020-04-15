# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None:
            return None

        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]

        while n != 1:
            lists1, lists2 = self.mergeKLists(lists[:n/2]), self.mergeKLists(lists[n/2:])
            return self.merge2Lists(lists1, lists2)

    def merge2Lists(self, l1, l2):
        prehead = ListNode(-1)

        ptr = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next

            ptr = ptr.next

        # after loop finished, node1 or node2 should have one which is not None
        # append it to the end
        ptr.next = l1 if l1 is not None else l2

        return prehead.next
