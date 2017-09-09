class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if zeros == 0:
                    zeros+=1
                    i+=1
                else:
                    zeros+=1

            else:
                nums[i],nums[i-zeros] = nums[i-zeros],nums[i]
                i+=1
        print(nums)

if __name__ == '__main__':
    s= Solution()
    s.moveZeroes([0, 1, 0,0,0,13, 3, 12])
