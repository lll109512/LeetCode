class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        it = iter(t)
        """
        python中的iter 在 in 操作时会找到第一个匹配字符的位置，若不存在直接跑到结尾。
        eg.
        x =  [1,2,3,4]
        1 in x    #Ture  此时 x iter 为[2,3,4]
        1 in x    #False 因为没有找到 x iter 跑到末尾
        """
        return all(c in it for c in s)
