# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head

        tmp = head
        length = 0
        while tmp:
            length += 1
            tmp = tmp.next
            
        if length < k:
            return head
            
        def reverseLinkedList(head):
            prev = None
            cur = head
            next = head.next

            while next is not None:
                # reverse
                tmp = next.next
                next.next = cur
                cur.next = prev

                # pointer move
                prev = cur
                cur = next
                next = tmp

            return cur

        # devide list into valid sublists
        heads = [head]
        counter = 0
        h = head
        while h.next is not None:
            counter += 1
            if counter != k:
                h = h.next
                continue
            else:
                counter = 0
                tmp = h.next
                h.next = None
                h = tmp
                heads.append(h)

        if length%k != 0:
            lastHead = heads.pop()

        reversedHeads = map(reverseLinkedList, heads)
        reversedHeads.append(None)
        for i in xrange(len(heads)):
            heads[i].next = reversedHeads[i+1]

        if length%k != 0:
            heads[-1].next = lastHead

        return reversedHeads[0]
