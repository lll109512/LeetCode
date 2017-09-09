class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        H = len(M)
        W = len(M[0])
        return_M = [[0 for _ in range(W)] for _ in range(H)]
        M = [[-1 for _ in range(W)]] + M + [[-1 for _ in range(W)]]
        new_M = []
        for line in M:
            line = [-1] + line + [-1]
            new_M.append(line)
        for i in range(1,len(new_M)-1):
            for j in range(1,len(new_M[0])-1):
                c = []
                positon = [new_M[i-1][j-1],new_M[i-1][j],new_M[i-1][j+1],new_M[i][j-1],new_M[i][j],new_M[i][j+1],new_M[i+1][j-1],new_M[i+1][j],
                    new_M[i+1][j+1]]
                for k in positon:
                    if k != -1:
                        c.append(k)
                return_M[i-1][j-1] = sum(c)//len(c)
        # for line in return_M:
        #     print(line)
        return return_M



if __name__ == '__main__':
    s = Solution()
    s.imageSmoother([[1,1,1],
                    [1,0,1],
                    [1,1,1]])
