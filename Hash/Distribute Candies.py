class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        Total_len = len(candies)
        s = set(candies)
        Distribute_len = len(s)
        if Distribute_len<=Total_len/2:
            return Distribute_len
        else:
            return Total_len/2
