class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ht = {}
        for n in nums:
            ht[n] = True
        keys = ht.keys()
        best = 0
        for key in keys:
            if key - 1 not in keys:
                y = key+1
                while y in keys:
                    y+=1
                best = max(best,y-key)
        return best
