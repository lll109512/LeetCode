# #my version
# class Solution(object):
#     def twoSum(self,nums, target):
#         result = []
#         ht={}
#         for idx, num in enumerate(nums):
#             com = target - num
#             if com in ht.keys():
#                 return [ht[com],idx]
#             ht[num] = idx
#         return result
# #faster version
# class Solution2(object):
#     def twoSum(self,nums, target):
#         result = []
#         for idx, num in enumerate(nums):
#             nums[idx] = ''
#             if (target-num) in nums:
#                 result.append(idx)
#             nums[idx] = num
#         return result

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        D = {}
        L = []
        for num in array:
            rest = tsum - num
            # print(rest,num)
            if rest in D.keys():
                L.append([rest,num])
            D[num] = 1
        return min(L,key = lambda x : x[0]*[1])

if __name__ == '__main__':
    x=Solution()
    # print(x.twoSum([2,1,9,4,4,56,90,3],8))
    print(x.FindNumbersWithSum([1,2,4,7,11,15],15))
