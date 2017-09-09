class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def DFS(remain,accumulate):
            if all(x == 0 for x in remain):
                return accumulate
            elif any( x < 0 for x in remain):
                return float('inf')
            ans = sum(map(lambda x,y : x*y,price,remain))
            for spc in special:
                ans = min(ans,DFS(map(lambda x, y: x - y, remain,spc[:-1]),spc[-1]))
            return ans + accumulate
        return DFS(needs,0)
