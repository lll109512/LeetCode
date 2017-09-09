class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        #print(path.split('/'))
        for word in path.split('/'):
            if word=='' or word=='.':
                continue
            if word=='..':
                if len(stack)==0:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(word)
        if len(stack)==0:
            return '/'
        else:
            return '/'+'/'.join(stack)



if __name__ == '__main__':
    s=Solution()
    print(s.simplifyPath("/.."))
