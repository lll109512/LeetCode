class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 2
        s = 0
        while i <= n:
            while n % i == 0:
                s += i
                n /= i
            i+=1
        return s




    def _re(self,copy,step,position):
        """
        copy :复制长度
        step :当前操作次数
        position: 当前位置
        2000:会超出深度
        """
        # print(position)
        if dp[position] < step:
            return
        else:
            dp[position] = step
        if copy + position > len(dp)-1:
            return
        else:
            self._re(copy,step+1,position+copy)
        copy = position+1
        if copy + position > len(dp)-1:
            return
        else:
            self._re(copy,step+2,position+copy)



if __name__ == '__main__':
    s = Solution()
    print(s.minSteps(15))
