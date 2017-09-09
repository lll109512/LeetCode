import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        combine=[[x,y] for x in nums1 for y in nums2]
        return heapq.nsmallest(k,combine,key=lambda combine:combine[1]+combine[0])




if __name__ == '__main__':
    s=Solution()
    s.kSmallestPairs([1,7,11],[2,4,6],3)
