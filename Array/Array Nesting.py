class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        visited = [False for _ in range(len(nums))]
        for i in range(len(nums)):
            cur = i
            l = 1
            if visited[i]:
                continue
            visited[i] = True
            while not nums[cur] == i:
                # print(nums[cur])
                l += 1
                cur = nums[cur]
                visited[cur] = True
            ans = max(ans,l)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.arrayNesting([5,4,0,3,1,6,2]))
