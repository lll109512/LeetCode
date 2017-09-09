from functools import reduce
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        ans = [3] * (n//3)
        rest = n%3
        if rest == 1:
            ans[0]+=1
        elif rest == 2:
            ans.append(2)
        return reduce(lambda a, b: a*b, ans)

if __name__ == '__main__':
    s = Solution()

    print(s.integerBreak(15))
