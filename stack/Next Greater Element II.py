class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                answer[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                answer[stack.pop()] = nums[i]
            if not stack:
                break
        return answer


if __name__ == '__main__':
    s= Solution()
    print(s.nextGreaterElement([1,3,2,1]))
