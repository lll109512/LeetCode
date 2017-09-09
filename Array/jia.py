class Solution:
    def Sum_Solution(self, n):
        # write code here
        if n:
            return self.Sum_Solution(n-1) + n
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    print(s.Sum_Solution(5))
