import heapq
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, s = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(l[0]*l[1]*l[2],s[0]*s[1]*l[0])
