class Solution(object):
    def size(self, n):
        cnt = 0
        while n != None:
            n = n.next
            cnt += 1
        return cnt

    def get(self, head, n):
        while n > 1:
            head = head.next
            n -= 1
        return head.val

    def addTwoNumbers(self, l1, l2):
        sz1, sz2 = self.size(l1), self.size(l2)
        carry = 0
        dummy = ListNode(-1)
        while sz1 > 0 or sz2 > 0 or carry != 0:
            d1 = self.get(l1, sz1) if sz1 > 0 else 0
            d2 = self.get(l2, sz2) if sz2 > 0 else 0
            nxt = ListNode((d1 + d2 + carry) % 10)
            carry = (d1 + d2 + carry) / 10
            tmp = dummy.next
            dummy.next = nxt
            nxt.next = tmp
            sz1 -= 1
            sz2 -= 1
        return dummy.next
