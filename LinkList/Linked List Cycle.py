# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if not head.next:
            return False
        point_1 = head
        point_2 = head.next
        while point_2:
            if point_1 == point_2:
                return True
            point_1 = point_1.next
            if point_2.next and point_2.next.next:
                point_2 = point_2.next.next
            else:
                return False
        
