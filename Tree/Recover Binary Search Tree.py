# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.recover(root,sorted(self.find_all_number(root),reverse=True))


    def recover(self,root,nums):
        if not root:
            return
        node=root.left
        if node:
            self.recover(node,nums)
        root.val=nums.pop()
        node=root.right
        if node:
            self.recover(node,nums)


    def find_all_number(self,root):
        re=[]
        if root.left:
            re+=self.find_all_number(root.left)
        if root.right:
            re+=self.find_all_number(root.right)
        return [root.val]+re


if __name__ == '__main__':
    s=Solution()
    root=TreeNode(0)
    root.left=TreeNode(1)
    root.right=TreeNode(2)
    s.recoverTree(root)
