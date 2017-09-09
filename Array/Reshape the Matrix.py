class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat=[]
        result=[]
        for line in nums:
            flat.extend(line)
        if len(flat) != r*c:
            return nums
        for row in range(r):
            result.append([])
            for colum in range(c):
                result[row].append(flat.pop(0))
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.matrixReshape([[1,2,6],[3,4,10]],3,2))
