from bisect import bisect_left
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(n^2)
        """

        if not nums:
            return 0
        DP = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                DP[i] = max(DP[i],DP[j]+1 if nums[i] > nums[j] else DP[i])
        print(DP)
        return max(DP)

class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []
        for num in nums:
            idx = bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        print(tails)
        return len(tails)


if __name__ == '__main__':
    s = Solution2()
    s.lengthOfLIS([1,1,1,1,1,1,1])
