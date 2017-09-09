class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

    def print(self):
        curr=self
        while curr:
            print(curr.val,end='->')
            curr=curr.next
        print()



class Solution(object):
    def reverse(self, head, n):
        """
        Reverses the first n nodes of the list starting at the specified head
        node. Returns a tuple (a, b, c) where a and b are the start and end of
        the reversed list. c is the length of the reversed portion of the list.
        """
        assert n > 0
        assert head is not None

        tail = head
        current = head.next
        length = n
        n -= 1
        #tail.print()
        # Reverse the list by going through it in forward order and prepending
        # each node to the front.
        while n > 0 and current is not None:
            #current.print()
            next = current.next
            #next.print()
            current.next = head
            #current.print()
            head = current
            current = next
            #current.print()
            n -= 1
        # Ensure the tail of the reversed list points to the next element.
        tail.next = current
        #tail.print()
        #head.print()
        return (head, tail, length - n)

    def reverseKGroup(self, head, k):
        """
        Reverses the list starting at the head node k nodes at a time. If the
        list length is not a multiple of k the trailing nodes at the end must
        remain in their original order.
        """
        sentinel = ListNode(None)
        sentinel.next = head
        current = sentinel

        while current is not None and current.next is not None:
            sublist = self.reverse(current.next, k)
            # Check if this is a trailing list with less than k nodes.
            if sublist[2] != k:
                # Reverse the list again to bring it back into original order.
                sublist = self.reverse(sublist[0], k)
            current.next = sublist[0]
            current = sublist[1]

        return sentinel.next




if __name__ == '__main__':
    x=ListNode(0)
    head=x
    for i in range(1,4):
        x.next=ListNode(i)
        x=x.next
    #head.print()
    s=Solution()
    y=s.reverseKGroup(head, 2)
    y.print()
