class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        soed = sorted(pairs,key=lambda x: x[1])
        print(soed)
        DP = [soed[0]]
        for i in range(len(soed)):
                if DP[-1][1] < soed[i][0]:
                    DP.append(soed[i])
        print(DP)
        return len(DP)

if __name__ == '__main__':
    s = Solution()
    print(s.findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))
