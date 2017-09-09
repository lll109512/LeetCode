class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,2,4,3,2]
        """
        slow = 0
        fast = 0
        finder = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                while slow != finder:
                    slow = nums[slow]
                    finder = nums[finder]
                    if slow == finder:
                        return finder
