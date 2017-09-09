# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        re=[]
        self._inorderTraversal(root,re)
        return re

    def _inorderTraversal(self, root, result):
        if root.left:
            self._inorderTraversal(root.left,result)
        result.append(root.val)
        if root.right:
            self._inorderTraversal(root.right,result)


#way two using stack, DFS
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack=[root]
        ans=[]


        while stack:
            ro=stack.pop()
            if isinstance(ro,int):
                ans.append(ro)
                continue
            #beacuse stack LIFO, so we need swithc right and left
            #to make sure output with correct order
            if ro.right:
                stack.append(ro.right)
            stack.append(ro.val)
            if ro.left:
                stack.append(ro.left)

        return ans
