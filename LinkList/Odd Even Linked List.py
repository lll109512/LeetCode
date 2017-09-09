class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            odd_node_head = head
            pre_on = odd_node_head
        else:
            return None
        if head.next:
            even_node_head = head.next
            pre_en = even_node_head
        else:
            return head
        pnode = head.next.next
        i = 1
        while pnode:
            if i%2 == 1:
                pre_on.next = pnode
                pre_on = pre_on.next
            else:
                pre_en.next = pnode
                pre_en = pre_en.next
            pnode = pnode.next
            i+=1
        pre_en.next = None
        pre_on.next = even_node_head
        return odd_node_head
