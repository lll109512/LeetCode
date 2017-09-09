# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return None
        carry=0
        rlt_link=ListNode(0)
        head=rlt_link
        while l1:
            if not l2:
                while l1:
                    if (l1.val+carry)//10>0:
                        rlt_link.next=ListNode((l1.val+carry)%10)
                        carry=(l1.val+carry)//10
                    else:
                        rlt_link.next=ListNode(l1.val+carry)
                        carry=0
                    rlt_link=rlt_link.next
                    l1=l1.next
                if carry>0:
                    rlt_link.next=ListNode(carry)
                return head.next
            if (l1.val+l2.val+carry)//10>0:
                rlt_link.next=ListNode((l1.val+l2.val+carry)%10)
                carry=(l1.val+l2.val+carry)//10
            else:
                rlt_link.next=ListNode(l1.val+l2.val+carry)
                carry=0
            l1=l1.next
            l2=l2.next
            rlt_link=rlt_link.next
        while l2:
            if (l2.val+carry)//10>0:
                rlt_link.next=ListNode((l2.val+carry)%10)
                carry=(l2.val+carry)//10
            else:
                rlt_link.next=ListNode(l2.val+carry)
                carry=0
            rlt_link=rlt_link.next
            l2=l2.next
        if carry>0:
            rlt_link.next=ListNode(carry)
        return head.next



if __name__ == '__main__':
    pass
