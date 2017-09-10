class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 0
        R = len(nums) - 1
        while L < R:
            mid = (L + R)//2
            print(L,R,mid)
            if nums[mid] > nums[R]:
                L = mid+1
            else:
                R = mid

        return nums[L]



s = Solution()
s.findMin([5,6,7,0,1,2])
