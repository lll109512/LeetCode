# class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        md = self.depth(root)
        return self.find(root,md)

    def depth(self,root):
        if not root:
            return 0
        return max(self.depth(root.left),self.depth(root.right))+1

    def find(self,root,mdepth):
        if not root:
            return None
        if mdepth == 1:
            return root.val
        left = self.find(root.left,mdepth-1)
        right = self.find(root.right,mdepth-1)
        if left != None:
            return left
        else:
            return right
