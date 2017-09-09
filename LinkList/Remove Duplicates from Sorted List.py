class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        pre = head
        current = head.next
        while current:
            while current and pre.val == current.val:
                current = current.next
            if not current:
                pre.next = None
                break
            pre.next = current
            pre = current
            current = current.next
        return head
