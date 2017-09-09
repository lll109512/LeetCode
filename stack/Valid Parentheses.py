class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dty=dict({'(':')','{':'}','[':']'})
        stack=[]
        for item in s:
            #print(item)
            #print(stack)
            if item in dty:
                stack.append(item)
            elif len(stack)==0:
                return False
            else:
                if dty[stack.pop()]!=item:
                    return False
        return True if len(stack)==0 else False


if __name__ == '__main__':
    s=Solution()
    print(s.isValid("({})[]"))
