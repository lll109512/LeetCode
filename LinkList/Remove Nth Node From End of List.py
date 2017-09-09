# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        sz=self.size(head)
        count=sz-n-1
        dummy=head
        while count>0:
            dummy=dummy.next
            count-=1
        if count==-1:
            head=head.next
        else:
            if dummy.next and dummy.next.next:
                dummy.next=dummy.next.next
            elif dummy.next:
                dummy.next=None
        return head


    def size(self,n):
        count=0
        while n:
            count+=1
            n=n.next
        return count
