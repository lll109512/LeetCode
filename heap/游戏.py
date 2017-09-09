from __future__ import print_function, division
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0 or m == 0:
            return -1
        child = [i for i in range(n)]
        curr=0
        i = 0
        while len(child)>1:
            curr = ((m-1) % (n-i) + curr) % (n-i)
            print(curr)
            i+=1
            del child[curr]
        return child[0]


if __name__ == '__main__':
    s = Solution()
    print(s.LastRemaining_Solution(5,3) )
