class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        stack = []
        answer = []
        for x in nums:
            while len(stack) and stack[-1] < x:
                d[stack.pop()] = x
            stack.append(x)
        for y in findNums:
            answer.append(d.get(y,-1))
        return answer
