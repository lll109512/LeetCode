# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        maxnum = max(nums)

        root = TreeNode(maxnum)
        index = nums.index(maxnum)
        root.left = self.subtree(root.left,nums[:index])
        root.right = self.subtree(root.right,nums[index+1:])
        return root


    def subtree(self,root,array):
        # print(array)
        if not array:
            return None
        maxnum = max(array)
        # print(maxnum)
        subroot = TreeNode(maxnum)
        index = array.index(maxnum)
        subroot.left = self.subtree(subroot.left,array[:index])
        subroot.right = self.subtree(subroot.right,array[index+1:])
        return subroot


if __name__ == '__main__':
    s = Solution()
    s.constructMaximumBinaryTree([3,2,1,6,0,5])
