from collections import Counter
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = Counter()
        d[0] = 1
        ans = 0
        su = 0
        for num in nums:
            su += num
            ans += d[su - k]
            d[su] += 1
        return ans


s = Solution()
print(s.subarraySum([1,1,1,-1,1,-1,1],1))
