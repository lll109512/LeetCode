from functools import reduce
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        超深度
        """
        dp = {}
        if not nums:
            return 0
        nums.sort(reverse=True)
        def sub_p(target):
            if (target) not in dp:
                r = 0
                if target == 0:
                    r = 1
                elif target < 0:
                    return 0
                else:
                    r = sum(map(lambda b: sub_p(b), map(lambda b: target-b,nums)))
                dp[target] = r
            print(dp)
            return dp[target]

        return sub_p(target)

class Solution2(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [1] + [0] * target
        for i in range(1,len(dp)):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i-num]
        # print(dp)
        return dp[target]



if __name__ == '__main__':
    s = Solution2()
    print(s.combinationSum4([3,33,333],10000))
