import itertools
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return list(filter(lambda x:sum(x) == n,itertools.combinations([1,2,3,4,5,6,7,8,9],k)))




if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3,7))
