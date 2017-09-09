#python2.7
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Input: [7, 1, 5, 3, 6, 4]
        Output: 5
        max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
        """
        min_p,max_prof = float('inf') , 0
        for num in prices:
            min_p = min(min_p,num)
            prof = num - min_p
            max_prof = max(max_prof,prof)
        return max_prof



if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
