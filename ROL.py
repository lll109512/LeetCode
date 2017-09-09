class Solution:
    def ReverseSentence(self, s):
        if s == " ":
            return " "
        list = s.split()
        return ' '.join(list[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.ReverseSentence(' '))
