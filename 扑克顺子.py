class Solution:
    def IsContinuous(self, numbers):
        # write code here
        try:
            while 0 in numbers:
                numbers.remove(0)
        except Exception as e:
            pass
        numbers = sorted(numbers)
        if numbers[-1] - numbers[0]<5 and len(set(numbers)) == len(numbers):
            return True
        else:
            return False
        # inter = [numbers[i] - numbers[i-1] for i in range(1,len(numbers))]
        # if sum(inter) == 3:
        #     return True
     #   	elif sum(inter) == 4 and 0 not in D.keys():
        #     return True
        #
        # else:
        #     return False



if __name__ == '__main__':
    s = Solution()
    print(s.IsContinuous([0,3,2,6,4]))
