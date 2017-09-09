class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = {}
        def sub_maze(m,n):
            if (m,n) not in dp:
                if m < 0 or n < 0:
                    return 0
                if m == 0 and n == 0:
                    return 1
                r = sub_maze(m, n-1)+sub_maze(m-1, n)
                dp[(m,n)] = r
            return dp[(m,n)]

        ans = sub_maze(m-1,n-1)
        print(dp)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3,7))
