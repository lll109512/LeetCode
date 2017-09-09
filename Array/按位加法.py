class Solution:
    def Add(self, num1, num2):
        # write code here
        n1 = (num1&num2)<<1
        n2 = num1^num2
        while n1&n2:
            num1 = n1
            num2 = n2
            n1 = (num1&num2)<<1
            n2 = num1^num2
        return n1 | n2

class Solution2:
    def Add(self, num1, num2):
        # write code here
        if not num2:
            return num1
        return self.Add(num1^num2,(num1&num2)<<1)


if __name__ == '__main__':
    s = Solution()
    print(s.Add(-1,2))
