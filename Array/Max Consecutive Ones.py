class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX_number = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter +=1
                MAX_number = max(MAX_number,counter)
            else:
                counter = 0
        return MAX_number
