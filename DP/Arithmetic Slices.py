class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 1
        result = 0

        while i < len(A)-1 :
            point = i
            while point-1>=0 and point+1<len(A) and A[point] - A[point-1] == A[point+1] - A[point]:
                result+=1
                point+=1
            i+=1
        return result

#Faster
class Solution2(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        curr, result = 0,0
        for i in range(2,len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                curr+=1
                result+=curr
            else:
                curr=0
        return result


if __name__ == '__main__':
    s = Solution2()
    print(s.numberOfArithmeticSlices([1,2,3,4,5,6]))
