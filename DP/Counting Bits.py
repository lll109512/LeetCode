class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # iniArr = [0]
        # if num > 0:
        #     amountToAdd = 1
        #     while len(iniArr) < num + 1:
        #         print(iniArr)
        #         iniArr.extend([x+1 for x in iniArr])
        # return iniArr[0:num+1]
        # pre = []
        # for number in range(num+1):
        #     pre.append(sum([int(x) for x in list(bin(number))[2:]]))
        # return pre
        pre =[0]
        for i in range(1,num+1):
            pre.append(pre[i//2]+i%2)
        return pre



if __name__ == '__main__':
    s =Solution()
    print(s.countBits(7))
