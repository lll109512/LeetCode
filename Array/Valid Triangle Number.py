import itertools
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        over time limited
        """
        return len(list(filter(lambda x:x[0]+x[1]>x[2] and x[1]+x[2]>x[0] and x[2]+x[0]>x[1],itertools.combinations(nums,3))))

class Solution2(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        nums = sorted(nums)
        for i in range(len(nums)-1,-1,-1):
            left,right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    counter += right - left
                    right -= 1
                else:
                    left += 1
        return counter


if __name__ == '__main__':
    s = Solution()
    print(s.triangleNumber([2,2,3,4]))
