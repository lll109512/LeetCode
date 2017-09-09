import heapq
#or simple way
#class Solution(object):
#    def findKthLargest(self, nums, k):
#        """
#        :type nums: List[int]
#        :type k: int
#        :rtype: int
#        """
#
#        sort=sorted(nums)
#        return sort[-k]






#heap way
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(unms)
        re=heapq.nlargest(k,heapq)
        return re[-1]
