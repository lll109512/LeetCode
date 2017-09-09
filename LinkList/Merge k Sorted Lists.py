# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists)==0:
            return None
        return self.devide(lists)

    def devide(self,lists):
        if len(lists)==1:
            return lists[0]
        if len(lists)==2:
            return self.sub_merge(lists[0],lists[1])

        return self.sub_merge(self.devide(lists[:len(lists)//2]),self.devide(lists[len(lists)//2:]))



    def sub_merge(self,l1,l2):
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
