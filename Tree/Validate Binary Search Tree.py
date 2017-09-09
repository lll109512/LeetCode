# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        node=root.left
        if node:
            while node.right:
                node=node.right
            if node.val>=root.val:
                return False
        node=root.right
        if node:
            while node.left:
                node=node.left
            if node.val<=root.val:
                return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
