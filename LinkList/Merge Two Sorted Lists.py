# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        Node=ListNode(0)
        head=Node
        while l1 and l2:
            if l1.val<l2.val:
                Node.next=l1
                l1=l1.next
            else:
                Node.next=l2
                l2=l2.next
            Node=Node.next
        if l1:
                Node.next=l1
        else:
                Node.next=l2
        return head.next
