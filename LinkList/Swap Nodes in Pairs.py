# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy=ListNode(0)
        dummy.next=head
        re=dummy
        while dummy.next.next:
            after=dummy.next.next.next
            dummy_next=dummy.next
            dummy_next2=dummy.next.next
            dummy.next=dummy_next2
            dummy.next.next=dummy_next
            dummy_next.next=after

            dummy=dummy.next.next
            if dummy.next==None:
                break
        return re.next
