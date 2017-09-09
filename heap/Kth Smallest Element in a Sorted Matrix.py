import heapq
#easy way with O(n)
#class Solution(object):
#    def kthSmallest(self, matrix, k):
#        """
#        :type matrix: List[List[int]]
#        :type k: int
#        :rtype: int
#        """
#        Li=[]
#        for line in matrix:
#            Li.extend(line)
#        Li.sort()
#        return Li[k-1]

#heap way
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        Li=[]
        for line in matrix:
            Li.extend(line)
        heapq.heapify(Li)
        length=len(Li)
        if k>(length//2):
            return heapq.nlargest(length-k+1,Li)[-1]
        else:
            return heapq.nsmallest(k,Li)[-1]
