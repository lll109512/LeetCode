class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        超时！！
        """
        ans = []
        memo = {}
        def sub_p(op,right):
            if right == len(nums):
                SUM = sum_helper(op, right)
                if SUM == S:
                    if op not in ans:
                        print(op,SUM)
                        ans.append(op)
                return
            sub_p(op+'+', right+1)
            sub_p(op+'-',right+1)

        def sum_helper(op,right):
            if right == 1:
                if op[0] == '+':
                    return nums[0]
                else:
                    return-nums[0]
            if op in memo:
                return memo[op]
            else:
                s = sum_helper(op[:-1],right-1)
                if op[-1] == '+':
                    s += nums[right-1]
                else:
                    s -= nums[right-1]
                memo[op] = s
                return s
        sub_p("",0)
        # print(memo)
        return len(ans)


class Solution2(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = {}
        def sub_p(index,S):
            if (index,S) not in dp:
                r = 0
                if index == len(nums):
                    if S == 0:
                        r = 1
                else:
                    r = sub_p(index+1, S+nums[index]) + sub_p(index+1, S-nums[index])
                dp[(index,S)] = r
            return dp[(index,S)]
        r = sub_p(0,S)
        for i in dp:
            print(dp)
        return r



if __name__ == '__main__':
    s = Solution2()
    print(s.findTargetSumWays([1,1,1,1,1],3))
