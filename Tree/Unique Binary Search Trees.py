class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        Sum=0
        if n==1 or n==0:
            return 1
        if n%2==0:
            for i in range(0,n//2):
                Sum+=2*self.numTrees(i)*self.numTrees(n-1-i)
            return Sum
        else:
            for i in range(0,n//2):
                Sum+=2*self.numTrees(i)*self.numTrees(n-1-i)
            return Sum+self.numTrees(n//2)*self.numTrees(n//2)


#faster Catalan sequence
#DP way
#f(n)=f(0)*f(n)+f(1)*f(n-1)......
#1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862
    def numTrees2(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n == 0: return 1
            #make sure first two number is 1
            dp = [0 if _ > 1 else 1 for _ in range(n+1)]
            for i in range(2, n+1):
                for j in range(0, i):
                    dp[i] += dp[j] * dp[i-1-j]
            return dp[-1]


if __name__ == '__main__':
    s=Solution()
    print(s.numTrees2(1))
