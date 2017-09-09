class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[-1]
        heights.append(0)
        best=0
        for i in range(len(heights)):
            while heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                w=i-stack[-1]-1
                best=max(best,h*w)
                print(best,i,h,w)
            stack.append(i)
        return best

if __name__ == '__main__':
    s=Solution()
    s.largestRectangleArea([2,1,5,6,2,3])
