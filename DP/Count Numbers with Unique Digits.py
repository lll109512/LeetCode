from collections import Counter
from functools import reduce
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = 0
        for i in range(1,pow(10,n)):
            if any(x > 1 for x in Counter(str(i)).values()):
                b+=1
        return pow(10,n) - b



class Solution2(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        ans = 10
        for i in range(2,n+1):
            l = [9]+[10-x for x in range(1,i)]
            ans += reduce(lambda a,b:a*b, l)
        return ans






if __name__ == '__main__':
    s = Solution2()
    print(s.countNumbersWithUniqueDigits(2))
