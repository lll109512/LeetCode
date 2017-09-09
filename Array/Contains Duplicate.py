class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = set()
        for num in nums:
            if num in d:
                return True
            d.add(num)
        return False
