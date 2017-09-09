class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp = []
        def sub_p(nums):
            if nums in dp:
                return
            else:
                dp.append(nums)
                if nums:
                    for i in range(len(nums)):
                        sub_p(nums[:i] + nums[i+1:])
        sub_p(nums)
        return dp

class Solution2(object):
    """
    循环，能稍微快一点。
    """
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))
