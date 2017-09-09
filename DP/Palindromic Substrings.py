class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        None DP,O(n^2)time and O(n) space
        """
        N = len(s)
        result = 0
        for i in range(N*2+1):
            left = i//2
            right = left + i%2
            while left>=0 and right<N and s[left] == s[right]:
                result+=1
                left-=1
                right+=1
        # for x in result_list:
        #     print(x)
        return result

# class Solution(object):
#     def countSubstrings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         None DP,O(n^2)time and O(n) space
#         """

if __name__ == '__main__':

    s = Solution()
    print(s.countSubstrings(''))
