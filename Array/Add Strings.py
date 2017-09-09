class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = ''
        upper = 0
        if len(num1)<len(num2):
            num1, num2 = num2, num1
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            if i < len(num2):
                if upper+int(num1[i])+int(num2[i]) >=10:
                    remainder = (upper+int(num1[i])+int(num2[i])) % 10
                    upper = 1
                    ans = str(remainder) + ans
                else:
                    remainder = upper+int(num1[i])+int(num2[i])
                    upper = 0
                    ans = str(remainder) + ans
            else:
                if upper+int(num1[i]) == 10:
                    ans = '0'+ans
                    upper = 1
                else:
                    ans = str(int(num1[i]) + upper) + ans
                    upper = 0
        if upper ==1:
            ans = '1'+ans
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.addStrings('9'*5000,'1'*2000))
