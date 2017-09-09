class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def curt_max(left,right,memo):
            if left == right:
                return nums[left]
            if left > right:
                return 0
            if not (left,right) in memo:
                ss = sum(nums[left:right+1])
                value = max(ss-curt_max(left+1,right,memo) + nums[left],ss-curt_max(left,right-1,memo) + nums[right])
                memo[(left,right)] = value
            print(memo)
            return memo[(left,right)]
        s = sum(nums)
        p1 = curt_max(0, len(nums)-1, {})
        return p1 >= s - p1


if __name__ == '__main__':
    s = Solution()
    print(s.PredictTheWinner([1, 5, 233, 7]))
