class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        output = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            output[i] = p
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= p
            p *= nums[i]
        return output


if __name__ == '__main__':
    s = Solution()
    s.productExceptSelf([1,2,3,4])
